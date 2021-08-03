def pillow(s):
    x = list(s[0])
    y = list(s[1])
    z = 0
    while z < len(x):
        if x[z] == 'n':
            if y[z] == 'B':
                return True
        z += 1
    return False
