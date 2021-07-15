def switch_lights(a):
    s = sum(a)
    for i in range(len(a)):
        if s%2:
            s -= a[i]
            a[i] = 1-a[i]
        else:
            s -= a[i]
    return a
