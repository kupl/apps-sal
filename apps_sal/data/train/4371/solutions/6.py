def digits(num):
    return [int(x) + int(y) for i, x in enumerate(str(num)) for j, y in enumerate(str(num)) if j > i]
