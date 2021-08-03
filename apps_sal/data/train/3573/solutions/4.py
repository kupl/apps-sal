def solve(arr):
    largest = max(arr)
    all = sum(arr)

    return all // 2 if largest <= all - largest else all - largest
