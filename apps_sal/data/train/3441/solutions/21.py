def get_average(marks):
    num = 0
    for i in marks:
        num += i
    return int(num / len(marks))
