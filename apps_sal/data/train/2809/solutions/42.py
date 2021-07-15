def digitize(n):
    num = []
    z = str(n)
    for i in z:
        num.append(int(i))
    return num[::-1]
