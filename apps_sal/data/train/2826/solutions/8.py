def pyramid(n):
    pyramidArray = [[]] * n
    if n == 0:
        return []
    for i in range(0, n):
        l = [1] * int(i + 1)
        pyramidArray[i] = l
    return pyramidArray
