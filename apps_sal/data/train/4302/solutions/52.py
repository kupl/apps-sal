def better_than_average(classmates, you):
    res = sum(classmates) / len(classmates)
    if res < you:
        return True
    else:
        return False
