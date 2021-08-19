def get_average(marks):
    average = 0
    for a in marks:
        average += a
    return int(average / len(marks))
