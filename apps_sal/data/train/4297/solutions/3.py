from statistics import mean

def get_mean(arr, x, y):
    if all(1 < i < len(arr) + 1 for i in (x, y)):
        return mean((mean(arr[:x]), mean(arr[-y:])))
    return -1
