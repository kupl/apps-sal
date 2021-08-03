for _ in range(int(input())):
    n, s = tuple(map(int, input().split()))
    p = list(map(int, input().split()))
    isattacker = list(map(int, input().split()))
    minatk = 101
    mindef = 101
    for pos, price in zip(isattacker, p):
        if pos == 1 and minatk > price:
            minatk = price
        elif pos == 0 and mindef > price:
            mindef = price
    if s + minatk + mindef <= 100:
        print('yes')
    else:
        print('no')
