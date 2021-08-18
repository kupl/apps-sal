def find_average(num):
    sum = 0
    for i in num:
        sum += i
        average = sum / len(num)
    return average
