def switch_lights(a):
    s = sum(a)
    result = []
    for i in range(len(a) - 1):
        s -= a[i]
        result.append(s % 2)
    return result + [0]
