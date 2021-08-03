def scf(arr):
    return next((i for i in range(2, min(arr, default=1) + 1)if all(x % i == 0 for x in arr)), 1)
