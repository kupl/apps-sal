def encode(n, strng):
    for _ in range(n):
        (wos, spa, new, a) = ('', [], '', [])
        for i in range(len(strng)):
            if strng[i] == ' ':
                spa.append(i)
            else:
                wos += strng[i]
        shifted = []
        for i in range(len(wos)):
            shifted.insert((i + n) % len(wos), wos[i])
        for i in spa:
            shifted.insert(i, ' ')
        for i in [i for i in ''.join(shifted).split(' ')]:
            tem = []
            for j in range(len(i)):
                tem.insert((j + n) % len(i), i[j])
            a.append(''.join(tem))
        strng = ' '.join(a)
    return '{} {}'.format(n, strng)


def decode(strng):
    n = int(strng.split(' ')[0])
    strng = strng[len(str(n)) + 1:]
    for _ in range(n):
        (a, spa) = ([], [])
        for i in range(len(strng)):
            if strng[i] == ' ':
                spa.append(i)
        for i in [i for i in strng.split(' ')]:
            tem = []
            for j in range(len(i)):
                tem.insert((j - n) % len(i), i[j])
            a.append(''.join(tem))
        (wos, shifted) = (''.join(a), [])
        for i in range(len(wos)):
            shifted.insert((i - n) % len(wos), wos[i])
        for i in spa:
            shifted.insert(i, ' ')
        strng = ''.join(shifted)
    return strng
