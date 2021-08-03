def find_average(array):
    if len(array) < 1:
        return 0
    else:
        return sum(array) / len(array)
