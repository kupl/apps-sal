def solve(arr):
    (a, b, c) = sorted(arr)
    return (a + b + min(a + b, c)) // 2
