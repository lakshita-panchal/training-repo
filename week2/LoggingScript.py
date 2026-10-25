import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

dataset = [3, 9, 2, 1, 4, 8, 5, 7, 6]

built_in_sorted = dataset.copy()
built_in_sorted.sort()
logging.info(f"Built-in sort completed: {built_in_sorted}")


def bubble_sort(arr):
    if not isinstance(arr, list):
        logging.error("Input data is not a list!")
        return None
        
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    logging.info("Bubble sort finished successfully.")
    return arr


custom_sorted = bubble_sort(dataset.copy())
print("Final Output:", custom_sorted)

