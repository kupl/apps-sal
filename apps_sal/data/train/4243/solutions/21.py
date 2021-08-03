def find_average(array):

    sum = 0
    average = 0

    if (len(array) > 0):

        for number in array:
            sum += number

    else:
        return 0

    average = sum / len(array)

    return average
