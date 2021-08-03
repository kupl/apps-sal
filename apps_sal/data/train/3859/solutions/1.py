def odd_one(arr):
    return next((i for i, v in enumerate(arr) if v & 1), -1)
