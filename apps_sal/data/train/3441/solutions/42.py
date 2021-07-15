def get_average(marks):
    y = 0
    for n in range(len(marks)):
        y = y + marks[n-1]
    return int(y / len(marks))
