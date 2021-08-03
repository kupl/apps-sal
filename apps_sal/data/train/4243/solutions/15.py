def find_average(array):
    if not array:
        return 0
    else:
        sum = 0
        for i in array:
            sum += i
        return sum / len(array)
