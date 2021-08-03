def get_average(marks):
    total = 0
    x = 0
    for n in marks:
        total += marks[x]
        x += 1

    return total // len(marks)
