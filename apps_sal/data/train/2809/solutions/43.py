def digitize(n):
    x = str(n)
    y = ""
    lst = []
    for char in x:
        y = char + y
    for char in y:
        lst.append(int(char))
    return lst
