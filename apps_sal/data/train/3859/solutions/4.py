def odd_one(lst):
    return next((i for i, n in enumerate(lst) if n % 2 == 1), -1)
