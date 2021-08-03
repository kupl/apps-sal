def get_average(marks):
    count = 0
    for i in range(len(marks)):
        count += marks[i]
    return round(count // len(marks))
