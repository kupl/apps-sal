def get_average(marks):
    total = 0
    for i in marks:
        total = total + i
    avg = total // len(marks)
    return avg
