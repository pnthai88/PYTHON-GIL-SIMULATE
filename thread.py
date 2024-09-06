import threading
import multiprocessing
import time

_TOTAL_THREADS_OR_PROCESSES = 10
_LOOP_COUNT = 9**8

# Function to perform a CPU-bound task
def cpu_bound_task():
    count = 0
    for i in range(_LOOP_COUNT):
        count += i

# Using threading to simulate GIL behavior
def simulate_with_threads():
    threads = []
    
    for i in range(_TOTAL_THREADS_OR_PROCESSES):
        thread = threading.Thread(target=cpu_bound_task)
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

# Using multiprocessing to bypass GIL
def simulate_with_multiprocessing():
    processes = []
    
    for i in range(_TOTAL_THREADS_OR_PROCESSES):
        process = multiprocessing.Process(target=cpu_bound_task)
        processes.append(process)
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()

if __name__ == "__main__":
    # Simulate with threads (GIL in effect)
    start_time = time.time()
    simulate_with_threads()
    end_time = time.time()
    print(f"Threading (GIL) execution time: {end_time - start_time:.2f} seconds")

    # Simulate with multiprocessing (no GIL interference)
    start_time = time.time()
    simulate_with_multiprocessing()
    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time:.2f} seconds")