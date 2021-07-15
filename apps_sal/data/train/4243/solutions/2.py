def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0
