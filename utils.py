def load_process_list(data):
    """
    Input: list of dicts
    Returns: list of Process objects
    """
    from .process import Process
    processes = []
    for item in data:
        processes.append(Process(
            pid=item["pid"],
            arrival=item["arrival"],
            burst=item["burst"],
            priority=item.get("priority", 0)
        ))
    return processes
