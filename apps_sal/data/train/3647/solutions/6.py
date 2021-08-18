
from random import randint


def zip_slices(arr):
    arr = sorted(arr)[::-1]
    res = []
    n = len(arr)
    m = n // 2
    mins = arr[m:][::-1]
    maxes = arr[:m]
    for a, b in zip(maxes, mins):
        res.extend([a, b])
    if n % 2:
        res.append(mins[-1])
    return res


def candle_pop(arr):
    candle = sorted(arr)
    res = []
    i = -1
    while candle:
        res.append(candle.pop(i))
        i = 0 if i else -1
    return res


def candle_index(arr):
    candle = sorted(arr)
    n = len(arr)
    a = 0
    z = n - 1
    res = []
    for i in range(n):
        if i % 2:
            res.append(candle[a])
            a += 1
        else:
            res.append(candle[z])
            z -= 1
    return res


def set_pop(arr):
    nums = set(arr)
    res = []
    i = 0
    while nums:
        if i % 2:
            n = min(nums)
        else:
            n = max(nums)
        res.append(n)
        nums.remove(n)
        i += 1
    return res


def solve(arr): return (zip_slices, candle_pop, candle_index, set_pop)[randint(0, 3)](arr)
