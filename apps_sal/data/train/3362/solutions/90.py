def sum_mix(arr):
    a = 0
    for el in arr:
        if el == int(el):
            a += el
        elif el == str(el):
            el = int(el)
            a += el
    return a
