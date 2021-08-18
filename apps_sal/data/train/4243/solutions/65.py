def find_average(list):
    avg = 0
    for i in range(len(list)):
        avg += list[i]
    return avg / len(list)
