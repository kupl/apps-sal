def check(px, x):
    if px[1] == x[1]:
        return x[2] - px[2] <= x[0] - px[0] and x[2] >= px[2]
    else:
        return x[2] - px[2] + 1 <= x[0] - px[0] and x[2] >= px[2]


def checkdouble(px, x):
    if px[3] == x[3]:
        return x[4] - px[4] <= x[0] - px[0] and x[4] >= px[4]
    else:
        return x[4] - px[4] + 1 <= x[0] - px[0] and x[4] >= px[4]


for _ in range(int(input())):
    px = [0, 1, 1, 2, 1]
    g = True
    for _ in range(int(input())):
        x = list(map(int, input().split()))
        if x[1] == x[3] and x[2] == x[4]:
            g = False
        if not g:
            continue
        g = check(px, x)
        if g:
            g = checkdouble(px, x)
        px = x
    if not g:
        print('no')
    else:
        print('yes')
