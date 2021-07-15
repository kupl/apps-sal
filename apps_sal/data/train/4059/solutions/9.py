def switch_lights(a):
    z = a[::-1]
    status = 0
    for i in range(len(z)):
        status = status + z[i]
        if status % 2 == 1:
            if z[i] == 1:
                z[i] = 0
            elif z[i] == 0:
                z[i] = 1
    return z[::-1]

