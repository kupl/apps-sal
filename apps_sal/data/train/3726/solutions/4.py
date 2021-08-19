from collections import deque


def sort_array(array):
    odd = deque(sorted((x for x in array if x % 2)))
    return [odd.popleft() if x % 2 else x for x in array]
