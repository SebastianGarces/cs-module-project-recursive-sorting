# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if arr == []:
        return -1

    min = start
    max = end
    middle = min + max // 2

    if arr[middle] == target:
        return middle

    if arr[middle] >= target:
        max = middle
        return binary_search(arr, target, min, max)
    else:
        min = middle
        return binary_search(arr, target, min, max)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
