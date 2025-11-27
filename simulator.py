from .fcfs import run_fcfs
from .srtf import run_srtf
from .priority_preemptive import run_priority_preemptive
from .mfq import run_mfq

def run_algorithm(alg, processes):
    if alg == "fcfs":
        return run_fcfs(processes)
    elif alg == "srtf":
        return run_srtf(processes)
    elif alg == "pp":
        return run_priority_preemptive(processes)
    elif alg == "mfq":
        return run_mfq(processes)
    else:
        raise ValueError("Invalid algorithm")
