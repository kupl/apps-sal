for _ in range(int(input())):
    (l, flip) = map(int, input().split())
    d = input()
    up = d.upper()
    lp = d.lower()
    ku = 0
    kl = 0
    for i in range(0, len(d)):
        if d[i] == up[i]:
            ku += 1
        else:
            kl += 1
    if ku <= flip and kl <= flip:
        print('both')
    elif ku <= flip:
        print('chef')
    elif kl <= flip:
        print('brother')
    else:
        print('none')
