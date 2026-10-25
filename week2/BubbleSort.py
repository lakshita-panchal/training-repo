dataset = [45, 12, 89, 7, 34, 23, 67, 91, 50]

# 1. Built-in Sort
built_in_sorted = dataset.copy()
built_in_sorted.sort()
print("Built-in:", built_in_sorted)


# 2. Basic Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


custom_sorted = bubble_sort(dataset.copy())
print("Bubble Sort:", custom_sorted)

