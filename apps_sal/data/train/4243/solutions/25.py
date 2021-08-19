def find_average(a):
    for i in a:
        i += i
        y = i / len(a)
    return y
