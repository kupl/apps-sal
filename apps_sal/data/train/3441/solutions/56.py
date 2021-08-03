def get_average(marks):
    x = 0
    for i in marks:
        x += i
    x = x / len(marks)
    return int(x)
