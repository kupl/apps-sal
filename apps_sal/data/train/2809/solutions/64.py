def digitize(n):
    copy = []
    array = list(str(n))
    for num in array:
        copy.append(int(num))
    copy.reverse()
    return copy
