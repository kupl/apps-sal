def days_represented(trips):
    arr = [0] * 365
    for a, b in trips:
        arr[a:b + 1] = [1] * (b - a + 1)
    return sum(arr)
