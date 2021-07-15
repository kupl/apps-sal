def array_center(arr):
    m, a = min(arr), (sum(arr) / len(arr))
    return [n for n in arr if abs(n - a) < m]

