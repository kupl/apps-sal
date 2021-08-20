def switch_lights(a):
    i = len(a) - 1
    s = 0
    while i >= 0:
        if a[i]:
            s += 1
        if s:
            a[i] = (a[i] + s) % 2
        i -= 1
    return a
