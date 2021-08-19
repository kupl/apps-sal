def work_on_strings(a, b):
    z = []
    for i in a:
        x = i
        for j in b:
            if i.upper() == j or i.lower() == j:
                x = x.swapcase()
        z.append(x)
    k = []
    for i in b:
        x = i
        for j in a:
            if i.upper() == j or i.lower() == j:
                x = x.swapcase()
        k.append(x)
    return ''.join(z) + ''.join(k)
