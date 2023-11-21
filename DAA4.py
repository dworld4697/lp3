import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def randomized_quick_sort(arr):
    random.shuffle(arr)
    quick_sort(arr, 0, len(arr) - 1)

def analyze_sorting_algorithm(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    random.seed(42)
    array_size = 10000
    random_array = [random.randint(1, 100000) for _ in range(array_size)]
    deterministic_array = random_array.copy()

    print("Analyzing Deterministic Quick Sort:")
    deterministic_time = analyze_sorting_algorithm(quick_sort, deterministic_array)
    print(f"Deterministic Quick Sort took {deterministic_time:.6f} seconds")

    print("\nAnalyzing Randomized Quick Sort:")
    randomized_time = analyze_sorting_algorithm(randomized_quick_sort, random_array)
    print(f"Randomized Quick Sort took {randomized_time:.6f} seconds")
