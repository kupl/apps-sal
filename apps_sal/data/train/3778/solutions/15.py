import sys


def find_smallest_int(arr):
    smallest = sys.maxsize

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

    return smallest
