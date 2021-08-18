def find_average(lst):
    sum = 0
    for i in lst:
        sum += i
    return int(sum / len(lst))
