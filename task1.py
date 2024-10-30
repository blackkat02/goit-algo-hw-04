import timeit
import random
import matplotlib.pyplot as plt

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Insertion Sort implementation
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

# Timing function
def time_algorithm(algorithm, data):
    def wrapper():
        algorithm(data.copy())
    return wrapper

# Measure time for different data sizes
def measure_time(data_size):
    data_random = [random.randint(0, 10000) for _ in range(data_size)]
    data_sorted = sorted(data_random)
    data_reverse = data_sorted[::-1]
    data_nearly_sorted = data_sorted[:int(data_size * 0.9)] + random.sample(data_sorted[int(data_size * 0.9):], int(data_size * 0.1))

    timings = {}

    print(f"\nResults for data size: {data_size}")

    # Random data
    timings['Merge Sort (random)'] = timeit.timeit(time_algorithm(merge_sort, data_random), number=1)
    print(f"Merge Sort (random): {timings['Merge Sort (random)']} seconds")
    timings['Insertion Sort (random)'] = timeit.timeit(time_algorithm(insertion_sort, data_random), number=1)
    print(f"Insertion Sort (random): {timings['Insertion Sort (random)']} seconds")
    timings['Timsort (random)'] = timeit.timeit(time_algorithm(sorted, data_random), number=1)
    print(f"Timsort (random): {timings['Timsort (random)']} seconds")

    # Sorted data
    timings['Merge Sort (sorted)'] = timeit.timeit(time_algorithm(merge_sort, data_sorted), number=1)
    print(f"Merge Sort (sorted): {timings['Merge Sort (sorted)']} seconds")
    timings['Insertion Sort (sorted)'] = timeit.timeit(time_algorithm(insertion_sort, data_sorted), number=1)
    print(f"Insertion Sort (sorted): {timings['Insertion Sort (sorted)']} seconds")
    timings['Timsort (sorted)'] = timeit.timeit(time_algorithm(sorted, data_sorted), number=1)
    print(f"Timsort (sorted): {timings['Timsort (sorted)']} seconds")

    # Reverse sorted data
    timings['Merge Sort (reverse)'] = timeit.timeit(time_algorithm(merge_sort, data_reverse), number=1)
    print(f"Merge Sort (reverse): {timings['Merge Sort (reverse)']} seconds")
    timings['Insertion Sort (reverse)'] = timeit.timeit(time_algorithm(insertion_sort, data_reverse), number=1)
    print(f"Insertion Sort (reverse): {timings['Insertion Sort (reverse)']} seconds")
    timings['Timsort (reverse)'] = timeit.timeit(time_algorithm(sorted, data_reverse), number=1)
    print(f"Timsort (reverse): {timings['Timsort (reverse)']} seconds")

    # Nearly sorted data
    timings['Merge Sort (nearly sorted)'] = timeit.timeit(time_algorithm(merge_sort, data_nearly_sorted), number=1)
    print(f"Merge Sort (nearly sorted): {timings['Merge Sort (nearly sorted)']} seconds")
    timings['Insertion Sort (nearly sorted)'] = timeit.timeit(time_algorithm(insertion_sort, data_nearly_sorted), number=1)
    print(f"Insertion Sort (nearly sorted): {timings['Insertion Sort (nearly sorted)']} seconds")
    timings['Timsort (nearly sorted)'] = timeit.timeit(time_algorithm(sorted, data_nearly_sorted), number=1)
    print(f"Timsort (nearly sorted): {timings['Timsort (nearly sorted)']} seconds")

    return timings

# Measure and visualize the results
data_sizes = [100, 10000]
results = {}

for size in data_sizes:
    results[size] = measure_time(size)

# Visualization
def plot_timings(results, size):
    algorithms = list(results[size].keys())
    times = list(results[size].values())

    plt.figure(figsize=(10, 6))
    plt.barh(algorithms, times, color='skyblue')
    plt.xlabel('Time (seconds)')
    plt.title(f'Algorithm Performance for {size} Elements')
    plt.tight_layout()
    plt.show()

# Plot results for both small and large data sizes
plot_timings(results, 100)  # Small data size
plot_timings(results, 10000)  # Large data size
