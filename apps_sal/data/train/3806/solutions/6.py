from re import findall


def black_and_white(height, width, compressed):

    compr = ''.join(('0' if i % 2 else '1') * v for i, v in enumerate(compressed))

    res = []

    for i in range(0, len(compr), width):
        row, temp, black = compr[i: i + width], [], True

        m = [(c, len(g)) for g, c in findall(r'((.)\2*)', row)]
        for dig, n in m:
            if black and dig == '0':
                temp.extend([0, n])
                black == False
            elif not black and dig == '1':
                temp.extend([n, 0])
                black = True
            else:
                temp.append(n)
                black = not black

        if len(temp) % 2:
            temp.append(0)
        res.append(temp)

    return res
