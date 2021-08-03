def solve(arr):
    return [sorted(arr)[::-1][(-1)**i * i // 2] for i in range(len(arr))]
