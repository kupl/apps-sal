def switch_lights(a):
    i, l = sum(a) % 2, []
    for n in a:
        i ^= n
        l.append(i)
    return l
