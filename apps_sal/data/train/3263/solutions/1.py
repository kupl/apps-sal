def solve(arr):
    arr = sorted(int(m[:2]) * 60 + int(m[3:]) for m in set(arr))
    arr += [arr[0] + 1440]
    h, m = divmod(max(arr[i + 1] - arr[i] - 1 for i in range(len(arr) - 1)), 60)
    return "{:02}:{:02}".format(h, m)
