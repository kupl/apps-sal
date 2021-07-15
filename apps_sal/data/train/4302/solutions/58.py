def better_than_average(a, b):
    if sum(a) / len(a) < b:
        return True
    return False
