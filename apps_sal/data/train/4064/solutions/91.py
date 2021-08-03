def count_by(x, n):
    count = 1
    value = 0
    numberList = []
    while count <= n:
        value = value + x
        numberList.append(value)
        count = count + 1
    return numberList
