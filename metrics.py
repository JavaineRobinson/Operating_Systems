def compute_metrics(processes, total_time, cpu_busy_time):
    results = {}

    waiting_times = []
    turnaround_times = []
    response_times = []

    for p in processes:
        turnaround = p.finish_time - p.arrival
        waiting = turnaround - p.burst
        response = p.start_time - p.arrival

        turnaround_times.append(turnaround)
        waiting_times.append(waiting)
        response_times.append(response)

    results["avg_waiting"] = sum(waiting_times)/ len(processes)
    results["avg_turnaround"] = sum(turnaround_times) / len(processes)
    results["avg_response"] = sum(response_times) / len(processes)
    results["cpu_utilization"] = (cpu_busy_time / total_time) * 100
    results["throughput"] = len(processes) / total_time
    
    return results