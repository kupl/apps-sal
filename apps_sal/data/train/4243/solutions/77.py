def find_average(list):
    c = 0
    for i in list:
        i += i
        c += 1
    return i / c
