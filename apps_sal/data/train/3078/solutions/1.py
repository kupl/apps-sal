from statistics import mean


def array_center(arr):
    low, avg = min(arr), mean(arr)
    return [b for b in arr if abs(b - avg) < low]
