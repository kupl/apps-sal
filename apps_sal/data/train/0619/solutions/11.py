

for k in range(int(input())):
    p1, p2, w = map(int, input().split())

    u = p1 + p2
    u //= w
    if u % 2:
        print('COOK')
    else:
        print('CHEF')
