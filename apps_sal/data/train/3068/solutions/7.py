def vowel_back(st):
    s = ''
    for x in st:
        res = chr(ord('a') + (ord(x) - ord('a') + ((9, -1, -3)[(x == 'c') + (x == 'd') * 2], -(5, 1, 4)[(x == 'o') + (x == 'e') * 2])[x in 'aoiue']) % 26)
        if res in 'code':
            res = x
        s += res
    return s
