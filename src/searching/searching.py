def linear_search(arr, target):
    # Your code here
    for i, val in enumerate(arr):
        if val == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            right = mid - 1
        if target > arr[mid]:
            left = mid + 1

    return -1  # not found
