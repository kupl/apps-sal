def get_average(marks):
    sum = 0
    for score in marks:
        sum += score
    return int(sum / len(marks))

