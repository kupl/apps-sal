def get_average(marks):
    avg = 0
    for mark in marks:
        avg += mark
    avg /= len(marks)
    return int(avg)
