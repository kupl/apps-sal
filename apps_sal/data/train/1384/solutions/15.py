for _ in range(int(input())):
    (a, k) = map(int, input().split())
    inp = [int(i) for i in input()]
    conright = list(inp)
    prev = conright[0]
    for i in range(1, a):
        if conright[i] == 1:
            if prev == 1:
                conright[i] = conright[i - 1] + 1
            else:
                prev = conright[i]
        else:
            prev = conright[i]
    conleft = list(inp)
    prev = conleft[a - 1]
    for i in range(a - 2, -1, -1):
        if conleft[i] == 1:
            if prev == 1:
                conleft[i] = conleft[i + 1] + 1
            else:
                prev = conleft[i]
        else:
            prev = conleft[i]
    conright.insert(0, 0)
    conleft.append(0)
    m = -1
    for i in range(a - k + 1):
        insr = conright[i - 1]
        insl = conleft[i + k]
        m = max(m, k + conright[i] + conleft[i + k])
    print(m)
