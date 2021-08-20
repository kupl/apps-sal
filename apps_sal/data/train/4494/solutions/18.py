def points(games):
    l = []
    x = 0
    z = 0
    n = ' '.join(games)
    for i in n:
        if i != ' ' and i != ':':
            l.append(i)
            x += 1
            if x == 2:
                if int(l[0]) > int(l[1]):
                    z += 3
                elif int(l[0]) < int(l[1]):
                    z += 0
                else:
                    z += 1
                l.clear()
                x -= 2
    return z
