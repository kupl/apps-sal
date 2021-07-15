def solve(arr):
    arr = set(arr)
    return next(filter(lambda i :not (sum(arr) - i) ,arr))
