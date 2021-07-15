def digitize(n):
    empty = []
    n = str(n)
    n = n[::-1]
    for num in n:
        empty.append(int(num))
    return empty
