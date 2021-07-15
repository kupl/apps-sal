def odd_one(arr):
    return next((i for i, n in enumerate(arr) if n % 2), -1)
