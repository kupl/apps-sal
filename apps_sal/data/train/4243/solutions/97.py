def find_average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    total = sum / len(list)
    return total
