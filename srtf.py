import heapq


def run_srtf(process_list):
    """
    Run SRTF scheduling algorithm on a list of Process objects.
    Returns dict with 'gantt' and 'metrics' keys.
    """
    time = 0
    completed = 0
    n = len(process_list)
    ready_queue = []
    
    # Sort by arrival — needed for adding to queue
    processes = sorted(process_list, key=lambda p: p.arrival)
    
    i = 0  # index for arriving processes
    gantt_chart = []  # store (time, pid) for visualization
    cpu_busy = 0
    
    while completed < n:
        # Add all processes that arrive at the current time
        while i < n and processes[i].arrival == time:
            heapq.heappush(ready_queue, processes[i])
            i += 1
        
        # If no process is ready → CPU idle
        if not ready_queue:
            gantt_chart.append((time, "IDLE"))
            time += 1
            continue
        
        # Pick process with shortest remaining time
        current = heapq.heappop(ready_queue)
        
        # Record first start time for response time
        if current.start_time is None:
            current.start_time = time
        
        # Execute for 1 time unit
        current.remaining -= 1
        gantt_chart.append((time, current.pid))
        cpu_busy += 1
        time += 1
        
        # If process finished
        if current.remaining == 0:
            current.finish_time = time
            completed += 1
        else:
            # Put back with updated remaining time
            heapq.heappush(ready_queue, current)
    
    from .metrics import compute_metrics
    metrics = compute_metrics(processes, total_time=time, cpu_busy_time=cpu_busy)
    
    return {"gantt": gantt_chart, "processes": processes, "metrics": metrics}


def srtf_scheduling(process_list):
    time = 0
    completed = 0
    n = len(process_list)
    ready_queue = []

    # Sort by arrival — needed for adding to queue
    process_list.sort(key=lambda p: p.arrival)

    i = 0  # index for arriving processes

    gantt_chart = []  # store (time, pid) for visualization

    while completed < n:

        # Add all processes that arrive at the current time
        while i < n and process_list[i].arrival == time:
            heapq.heappush(ready_queue, process_list[i])
            i += 1

        # If no process is ready → CPU idle
        if not ready_queue:
            gantt_chart.append((time, "IDLE"))
            time += 1
            continue

        # Pick process with shortest remaining time
        current = heapq.heappop(ready_queue)

        # Record first start time for response time
        if current.start_time is None:
            current.start_time = time

        # Execute for 1 time unit
        current.remaining -= 1
        gantt_chart.append((time, current.pid))
        time += 1

        # If process finished
        if current.remaining == 0:
            current.completion = time
            completed += 1
        else:
            # Put back with updated remaining time
            heapq.heappush(ready_queue, current)

    # Calculate metrics
    results = []
    for p in process_list:
        turnaround = p.completion - p.arrival
        waiting = turnaround - p.burst
        response = p.start_time - p.arrival

        results.append({
            "PID": p.pid,
            "Arrival": p.arrival,
            "Burst": p.burst,
            "Completion": p.completion,
            "Turnaround": turnaround,
            "Waiting": waiting,
            "Response": response
        })

    return results, gantt_chart

"""
# Example usage
if __name__ == "__main__":
    processes = [
        Process("P1", 0, 8),
        Process("P2", 1, 4),
        Process("P3", 2, 9),
        Process("P4", 3, 5),
    ]

    results, chart = srtf_scheduling(processes)

    print("\n=== SRTF Scheduling Results ===")
    for r in results:
        print(r)

    print("\n=== Gantt Chart (Time → PID) ===")
    print(chart)
"""
