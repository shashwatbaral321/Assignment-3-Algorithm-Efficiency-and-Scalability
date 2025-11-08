import random
import time
import sys
import copy

# Set higher recursion depth for deep sorts
sys.setrecursionlimit(10000)

def partition(arr, low, high):
    """
    Lomuto partition scheme.
    Uses the element at arr[high] as the pivot.
    """
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element (arr[high]) into its final correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partition index

# --- Randomized Quicksort ---

def random_partition(arr, low, high):
    """
    Selects a random pivot, swaps it to the end, and partitions.
    """
    # Choose a random index between low and high (inclusive)
    rand_pivot_index = random.randint(low, high)

    # Move the random pivot to the end (high)
    arr[rand_pivot_index], arr[high] = arr[high], arr[rand_pivot_index]

    # Call the standard Lomuto partition
    return partition(arr, low, high)

def _randomized_quicksort(arr, low, high):
    """
    Recursive helper function for Randomized Quicksort.
    """
    if low < high:
        # pi is the partitioning index, arr[pi] is now at the right place
        pi = random_partition(arr, low, high)

        # Separately sort elements before partition and after partition
        _randomized_quicksort(arr, low, pi - 1)
        _randomized_quicksort(arr, high, pi + 1)

def randomized_quicksort(arr):
    """Entry function for Randomized Quicksort."""
    _randomized_quicksort(arr, 0, len(arr) - 1)

# --- Deterministic Quicksort (First Element Pivot) ---

def deterministic_partition(arr, low, high):
    """
    Uses the first element (arr[low]) as the pivot.
    We swap it to the end to use the same Lomuto logic.
    """
    # Move the first element (pivot) to the end
    arr[low], arr[high] = arr[high], arr[low]
    
    # Call the standard Lomuto partition
    return partition(arr, low, high)

def _deterministic_quicksort(arr, low, high):
    """
    Recursive helper function for Deterministic Quicksort.
    """
    if low < high:
        # pi is the partitioning index
        pi = deterministic_partition(arr, low, high)

        # Separately sort elements
        _deterministic_quicksort(arr, low, pi - 1)
        _deterministic_quicksort(arr, high, pi + 1)

def deterministic_quicksort(arr):
    """Entry function for Deterministic Quicksort."""
    _deterministic_quicksort(arr, 0, len(arr) - 1)

# --- Empirical Comparison ---

def run_experiment(sort_function, array, name):
    """
    Times a sorting function on a copy of the given array.
    """
    # Create a deep copy to not sort the original
    arr_copy = copy.deepcopy(array)
    
    start_time = time.perf_counter()
    try:
        sort_function(arr_copy)
    except RecursionError:
        print(f"Failed: {name} - RecursionError (likely O(n^2) behavior)")
        return
    end_time = time.perf_counter()
    
    print(f"Finished: {name}")
    print(f"  -> Time taken: {end_time - start_time: .6f} seconds")

if __name__ == "__main__":
    N = 5000  # Array size

    print(f"--- Running Quicksort Comparison (n={N}) ---")

    # 1. Randomly generated array
    random_arr = [random.randint(0, N * 10) for _ in range(N)]
    
    # 2. Already sorted array
    sorted_arr = list(range(N))
    
    # 3. Reverse-sorted array
    reverse_sorted_arr = list(range(N, 0, -1))
    
    # 4. Array with repeated elements
    repeated_arr = [random.randint(0, 10) for _ in range(N)]

    # --- Run Experiments ---
    
    print("\n[Test 1: Random Array]")
    run_experiment(randomized_quicksort, random_arr, "Randomized Quicksort")
    run_experiment(deterministic_quicksort, random_arr, "Deterministic Quicksort")

    print("\n[Test 2: Sorted Array]")
    run_experiment(randomized_quicksort, sorted_arr, "Randomized Quicksort")
    run_experiment(deterministic_quicksort, sorted_arr, "Deterministic Quicksort")

    print("\n[Test 3: Reverse-Sorted Array]")
    run_experiment(randomized_quicksort, reverse_sorted_arr, "Randomized Quicksort")
    run_experiment(deterministic_quicksort, reverse_sorted_arr, "Deterministic Quicksort")
    
    print("\n[Test 4: Array with Repeated Elements]")
    run_experiment(randomized_quicksort, repeated_arr, "Randomized Quicksort")
    run_experiment(deterministic_quicksort, repeated_arr, "Deterministic Quicksort")
