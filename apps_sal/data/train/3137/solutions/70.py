def round_it(n):
    addition = 0
    temp = str(n).split(".")
    if len(temp) != 2:
        return n
    if len(temp[0]) < len(temp[1]):
        return int(temp[0]) + 1
    if len(temp[0]) > len(temp[1]):
        return int(temp[0])
    return round(n)
