def find_average(a):
    s = 0
    avg = 0
    for i in a:
        s += i
    avg = s / len(a)
    return avg
