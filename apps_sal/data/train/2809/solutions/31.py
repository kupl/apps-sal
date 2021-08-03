def digitize(n):
    arr = []
    convertToString = str(n)
    for num in convertToString:
        arr.append(int(num))
    arr.reverse()
    return arr
