"""
Description:
Given an array/list [] of integers , Find the Nth smallest element in this array
of integers
"""
import random


def quick_select(arr, pos):
    pivot = random.choice(arr)
    less = []
    greater = []
    k = 0
    if len(arr) == 1:
        return arr[0]
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            k += 1
    if pos < len(less):
        return quick_select(less, pos)
    elif pos < len(less) + k:
        return pivot
    else:
        return quick_select(greater, pos - len(less) - k)


def nth_smallest(arr, pos):
    return quick_select(arr, pos - 1)


def __starting_point():
    print((nth_smallest([15, 20, 7, 10, 4, 3], 3)))


__starting_point()
