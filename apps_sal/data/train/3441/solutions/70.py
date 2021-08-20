def get_average(marks):
    tot = 0
    for i in marks:
        tot = tot + i
    avg = int(tot / len(marks))
    return avg
