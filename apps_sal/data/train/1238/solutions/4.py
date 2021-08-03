for t in range(int(input())):
    word = input()
    lis = list(word)
    d = {}
    for l in range(10):
        d[l] = None
    s = ''
    for w in lis:
        if d[int(w)] != None:
            d[int(w)] += 1
        else:
            d[int(w)] = 1

    for i in range(5, 10):
        if d[i] != None and i != 6 and d[6] != None:
            s = s + chr(60 + i)
        if d[i] != None and d[i] >= 2 and i == 6:
            s = s + chr(60 + i)
    for i in range(10):
        if d[i] != None and i != 7 and d[7] != None:
            s = s + chr(70 + i)
        if d[i] != None and d[i] >= 2 and i == 7:
            s = s + chr(70 + i)
    for i in range(10):
        if d[i] != None and i != 8 and d[8] != None:
            s = s + chr(80 + i)
        if d[i] != None and d[i] >= 2 and i == 8:
            s = s + chr(80 + i)
    if d[9] != None and d[0] != None:
        s = s + chr(90)
    if len(s) == 0:
        print()
    else:
        print(s)
