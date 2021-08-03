def get_average(marks):
    sum = 0
    for i in range(len(marks)):
        sum += marks[i]
        i += 1
    return int(sum / len(marks))
