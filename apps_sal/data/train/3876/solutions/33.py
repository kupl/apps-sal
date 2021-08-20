def find(n):
    x = 0
    for i in range(n):
        z = i + 1
        if z % 3 == 0 or z % 5 == 0:
            x += z
    return x
