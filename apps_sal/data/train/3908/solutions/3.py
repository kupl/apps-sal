def solve(arr):
    freq = {n: -arr.count(n) for n in set(arr)}
    return sorted(sorted(arr), key=freq.get)
