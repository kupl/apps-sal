def get_mean(arr, x, y):
    return -1 if x < 2 or y < 2 or x > len(arr) or (y > len(arr)) else (sum(arr[:x]) / float(x) + sum(arr[-y:]) / float(y)) / 2.0
