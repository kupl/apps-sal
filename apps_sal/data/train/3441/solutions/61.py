def get_average(marks):
    total = sum((e for e in marks))
    return int(total / len(marks))
