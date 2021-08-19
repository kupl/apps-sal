def find_average(lst):
    count = 0
    average = 0
    for i in lst:
        count += i
    average = count / len(lst)
    return average
