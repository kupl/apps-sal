def smallest_integer(matrix):
    r = [j for i in matrix for j in i]
    i = 0
    while True:
        if i not in r:
            return i
        i += 1
