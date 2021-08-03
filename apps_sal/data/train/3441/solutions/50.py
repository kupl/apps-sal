marks = [2, 5, 13, 20, 16, 16, 10]


def get_average(marks):
    sum = 0
    for mark in marks:
        sum = sum + mark
    return int(sum / len(marks))
