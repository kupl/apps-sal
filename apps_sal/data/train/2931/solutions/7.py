from collections import deque


def count_cows(n):
    if not isinstance(n, int):
        return None
    calves = deque([1, 0, 0])
    cows = 0
    for i in range(n):
        cows += calves.pop()
        calves.appendleft(cows)
    return cows + sum(calves)
