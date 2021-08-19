def digitize(n):
    lst = []
    n = str(n)
    for char in n:
        lst.append(int(char))
    lst = lst[::-1]
    return lst
