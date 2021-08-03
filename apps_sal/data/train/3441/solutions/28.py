def get_average(marks):
    mean = 0.0
    sum = 0
    for i in marks:
        sum += i
    mean = sum / len(marks)
    return int(mean)
