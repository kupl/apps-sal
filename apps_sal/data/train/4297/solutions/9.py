def get_mean(arr, x, y):
    if x <= 1 or y <= 1:
        return -1
    elif x > len(arr) or y > len(arr):
        return -1
    else:
        return 0.5 * (sum(arr[:x]) / x + sum(arr[-y::]) / y)
    # your code here
