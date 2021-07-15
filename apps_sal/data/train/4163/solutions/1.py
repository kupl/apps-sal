from itertools import accumulate

def is_centered(arr, n):
    xs = [0] + list(accumulate(arr))
    return any(b-a==n for a, b in zip(xs[:len(arr)//2+1], xs[::-1]))
