from collections import deque

def run_mfq(process_list, q1= 2, q2 =4):
    time = 0
    gantt = []
    cpu_busy = 0

    processes = sorted(process_list, key = lambda p: p.arrival)

    Q0 = deque()
    Q1 = deque()
    Q2 = deque()

    finished = 0
    n = len(processes)

    while finished < n:
        for p in processes:
            if p.arrival == time:
                Q0.append(p)
            
        current = None
        queue_level = None
        
        quantum = None
        if Q0:
            current = Q0[0]
            queue_level = 0
            quantum = q1
        elif Q1:
            current = Q1[0]
            queue_level = 1
            quantum = q2
        elif Q2:
            current = Q2[0]
            queue_level = 2
            quantum = current.remaining
        else:
            time += 1
            continue
        
        if current.start_time is None:
            current.start_time = time
        
        for _ in range (quantum):
            if current.remaining == 0:
                break

            gantt.append((time, current.pid))
            current.remaining -= 1
            cpu_busy += 1
            time += 1

            for p in processes:
                if p.arrival == time:
                    Q0.append(p)
        
        if current.remaining == 0:
            current.finish_time = time
            if queue_level == 0:
                Q0.popleft()
            elif queue_level == 1:
                Q1.popleft()
            else:
                Q2.popleft()
                finished += 1
        else:
            if queue_level == 0:
                Q0.popleft()
                Q1.append(current)
            elif queue_level == 1:
                Q1.popleft()
                Q2.append(current)
            else:
                pass

    from .metrics import compute_metrics
    metrics = compute_metrics(processes, total_time = time, cpu_busy_time = cpu_busy)

    return {"gantt": gantt, "processes": processes, "metrics": metrics}