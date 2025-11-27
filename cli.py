import json
from .utils import load_process_list
from .simulator import run_algorithm

def print_menu():
    print("\nCPU Scheduling Simulator")
    print("1) FCFS")
    print("2) Priority Preemptive")
    print("3) SRTF")
    print("4) MFQ")
    print("5) Run All & Compare")
    print("0) Exit")

def collect_processes():
    n = int(input("Number of processes: "))
    data = []
    for i in range(n):
        print(f"\nProcess {i+1}:")
        arrival = int(input("Arrival time: "))
        burst = int(input("Burst time: "))
        priority = int(input("Priority (lower = higher priority): "))
        data.append({"pid": i+1, "arrival": arrival, "burst": burst, "priority": priority})
    return load_process_list(data)

def show_results(result):
    print("\n=== GANTT CHART ===")
    print(result["gantt"])

    print("\n=== METRICS ===")
    for k, v in result["metrics"].items():
        print(f"{k}: {v:.2f}")

def main():
    while True:
        print_menu()
        choice = input("Select option: ")

        if choice == "0":
            break
        elif choice in ["1", "2", "3", "4", "5"]:
            processes = collect_processes()

            if choice == "1":
                result = run_algorithm("fcfs", processes)
                show_results(result)

            elif choice == "2":
                result = run_algorithm("pp", processes)
                show_results(result)

            elif choice == "3":
                result = run_algorithm("srtf", processes)
                show_results(result)

            elif choice == "4":
                result = run_algorithm("mfq", processes)
                show_results(result)

            elif choice == "5":
                for alg in ["fcfs", "pp", "srtf", "mfq"]:
                    print(f"\n=== ALGORITHM: {alg.upper()} ===")
                    result = run_algorithm(alg, processes)
                    show_results(result)
        else:
            print("Invalid option.")
