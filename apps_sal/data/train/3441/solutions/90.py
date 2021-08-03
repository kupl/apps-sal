def get_average(marks):
    length = len(marks)
    sum = 0
    for i in range(0, length):
        sum = sum + marks[i]

    return int(sum / length)
