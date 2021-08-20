def get_numbers(arr, target, cb):
    result = []
    for num in arr:
        if cb(num, target):
            result.append(num)
    return result


def is_less(a, b):
    return a < b


def is_greater(a, b):
    return a > b


def is_equal(a, b):
    return a == b


def get_less_numbers(arr, target):
    return get_numbers(arr, target, is_less)


def get_greater_numbers(arr, target):
    return get_numbers(arr, target, is_greater)


def get_equal_numbers(arr, target):
    return get_numbers(arr, target, is_equal)


def q_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = get_less_numbers(arr, pivot)
    greater = get_greater_numbers(arr, pivot)
    mypivot = get_equal_numbers(arr, pivot)
    return q_sort(less) + mypivot + q_sort(greater)


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        return q_sort(nums)
