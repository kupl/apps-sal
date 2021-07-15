def seven(m):
    if len(str(m)) <= 2 :
        return (0,0)
    counter = 0
    while len(str(m)) != 2:
        m = int(str(m)[:-1]) - int(str(m)[-1]) * 2
        counter += 1
        if len(str(m)) <= 2:
            break
    return (m,counter)

