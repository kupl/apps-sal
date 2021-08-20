for _ in range(int(input())):
    (n, m) = [int(x) for x in input().split()]
    command = input()
    maxL = 0
    maxR = 0
    hom = 0
    maxU = 0
    maxD = 0
    vem = 0
    for co in command:
        if co == 'L':
            hom += 1
        elif co == 'R':
            hom -= 1
        elif co == 'U':
            vem += 1
        else:
            vem -= 1
        if hom > maxL:
            maxL = hom
        if hom < maxR:
            maxR = hom
        if vem > maxU:
            maxU = vem
        if vem < maxD:
            maxD = vem
    if maxL - maxR < m and maxU - maxD < n:
        print('safe')
    else:
        print('unsafe')
