def switch_lights(a):
    S = sum(a) % 2
    for i in range(len(a)):
        (a[i], S) = ([a[i], 1 - a[i]][S == 1], [S, 1 - S][a[i] == 1])
    return a
