# Purpose of get_process data : Collect process burst time, arrival time, and priority
def get_process_data():
    #Accept the number of process from user
    num_of_process = int(input("Enter the number of Processes in the Scheduler: "))

    #List to store the attributes of the process entered
    burst_time = []
    arrival_time = []
    process_id = []
    priority = []

    #For loop to accept the bt,at,p for the amount of process inputted by the user
    for i in range(num_of_process):
        process_id.append(f"P{i}")  #Auto generate process ID
        
        #Output statements to collect info from user
        bt = int(input(f"Enter the Burst Time for Process - {i}: "))
        at = int(input(f"Enter the Arrival Time for Process - {i}: "))
        p = int(input(f"Enter the Priority for Process - {i}: "))

        #Add the process attributes to there designated list
        burst_time.append(bt)
        arrival_time.append(at)
        priority.append(p)

    #Return all process atrributes 
    return num_of_process, process_id, burst_time, arrival_time, priority

#this function sort processes based on arrival time using the Bubble Sort
def sort_arrivaltime(at, bt, pid, priority):
    n = len(at)

    for i in range(n):
        swapped = False

         # Compare each pair and swap if needed
        for j in range(n - i - 1):
            if at[j] > at[j + 1]: # Compare arrival times
                # Swap arrival times
                at[j], at[j + 1] = at[j + 1], at[j]
                 # Swap burst times
                bt[j], bt[j + 1] = bt[j + 1], bt[j]
                # Swap process IDs
                pid[j], pid[j + 1] = pid[j + 1], pid[j]
                # Swap priorities
                priority[j], priority[j + 1] = priority[j + 1], priority[j]
                
                swapped = True
        # If no swap happened, array is sorted quickly and exit early        
        if not swapped:
            break


#Implement First Come First Serve CPU scheduling algorithm
def fcfs(num_of_process, pid, burst_time, arrival_time, priority):
     # Make copies of input lists to avoid modifying original data
    bt = burst_time[:]
    at = arrival_time[:]
    id_list = pid[:]
    pr = priority[:]

   # Sort all processes based on arrival time
    sort_arrivaltime(at, bt, id_list, pr)

    # Initialize lists for scheduling results
    finish_time = [0] * num_of_process
    waiting_time = [0] * num_of_process
    turnaround_time = [0] * num_of_process

    # First process
    finish_time[0] = at[0] + bt[0]
    turnaround_time[0] = finish_time[0] - at[0]  # Turnaround = timme finish - Arrival
    waiting_time[0] = turnaround_time[0] - bt[0]  # waiting time = Turnaround - Burst

     # Remaining process starts after previous one finishes
    for i in range(1, num_of_process):
        finish_time[i] = finish_time[i - 1] + bt[i]
        turnaround_time[i] = finish_time[i] - at[i]
        waiting_time[i] = turnaround_time[i] - bt[i]

    # Calculate averages
    avg_waiting = sum(waiting_time) / num_of_process
    avg_turnaround = sum(turnaround_time) / num_of_process

    # Output results in a formatted table
    print("\nFCFS Scheduling Algorithm:")
    print(f"{'ProcessId':>12} {'BurstTime':>12} {'ArrivalTime':>12} "
          f"{'FinishTime':>12} {'WaitingTime':>12} {'TurnAroundTime':>16}")

    # Print metrics for each process
    for i in range(num_of_process):
        print(f"{id_list[i]:>12} {bt[i]:>12} {at[i]:>12} "
              f"{finish_time[i]:>12} {waiting_time[i]:>12} {turnaround_time[i]:>16}")

    # Print average metrics
    print(f"\n{'Average':>60} {avg_waiting:>12.2f} {avg_turnaround:>16.2f}")


def main():
    # Get process data from user
    n, pid, bt, at, priority = get_process_data()
    # Run FCFS scheduling algorithm
    fcfs(n, pid, bt, at, priority)


if __name__ == "__main__":
    main()
