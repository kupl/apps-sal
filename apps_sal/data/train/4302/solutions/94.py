def better_than_average(a, b):
    res = sum(a) / len(a)

    if res < b:
        return True
    else:
        return False
