def solve(arr):
    tmp = {}
    s = set(arr)
    for n in s:
        tmp[n] = [idx for (idx, num) in enumerate(arr) if num == n]
    ides = [value[-1] for value in tmp.values()]
    return [arr[idx] for idx in sorted(ides)]
