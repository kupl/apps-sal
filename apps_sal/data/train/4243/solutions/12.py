def find_average(array):
    sum = 0
    for num in array:
        sum += num
    try:
        return sum / len(array)
    except ZeroDivisionError:
        return 0
