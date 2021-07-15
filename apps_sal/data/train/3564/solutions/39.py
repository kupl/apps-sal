def stringy(size):
    x = 0
    list_size = []
    for i in range(size):
        if x % 2:
            i = 0
        else:
            i = 1
        x += 1
        list_size.append(i)
    return str(''.join(map(str, list_size)))
