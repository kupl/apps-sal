def get_average(marks):
    sum = 0
    for v in marks:
        sum += v
    average = int(sum / len(marks))
    return average
