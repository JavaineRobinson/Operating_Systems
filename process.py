class Process:
    def __init__(self, pid, arrival, burst, priority=0):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.priority = priority

        # Metrics
        self.start_time = None
        self.finish_time = None
        self.response_time = None
    
    # For PriorityQueue (min-heap): compare by remaining time (for SRTF)
    def __lt__(self, other):
        return self.remaining < other.remaining