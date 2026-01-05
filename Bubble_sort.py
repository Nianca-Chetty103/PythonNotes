def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps happened, array is already sorted
        if not swapped:
            break


# Example
nums = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(nums)
print(nums)
