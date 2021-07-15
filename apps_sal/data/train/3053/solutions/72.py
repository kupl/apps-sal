def close_compare(a, b, margin = 0):
    area = range((b - margin), (b + 1 + margin))
    if a in area:
        return 0
    elif a < (b - margin):
        return -1
    elif a > (b + margin):
        return 1
