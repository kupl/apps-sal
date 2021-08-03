def odd_one(arr):
    try:
        return next(i for i, x in enumerate(arr) if x % 2)
    except:
        return -1
