def repeats(arr):
    return sum(n for n in arr if arr.count(n) == 1)
