def find_average(x):
    y = 0
    for i in range(len(x)):
        y = y + x[i]
    return (y / len(x))
