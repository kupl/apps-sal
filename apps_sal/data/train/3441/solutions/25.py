def get_average(marks):
    total = 0
    for k in range(len(marks)):
        total += marks[k]
    return total // len(marks)

