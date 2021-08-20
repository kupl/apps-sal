def disarium_number(x):
    return 'Disarium !!' if [sum((int(e) ** (i + 1) for (i, e) in enumerate(str(x))))] == [x] else 'Not !!'
