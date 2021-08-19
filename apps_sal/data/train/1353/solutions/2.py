def check1(t, x, y, px, py):
    if x == px:
        return y - py <= t and py <= y
    return y - py + 1 <= t and py <= y


def check(px, x):
    t = x[0] - px[0]
    return check1(t, x[1], x[2], px[1], px[2]) and check1(t, x[3], x[4], px[3], px[4])


for _ in range(int(input())):
    px = [0, 1, 1, 2, 1]
    g = True
    for _ in range(int(input())):
        x = list(map(int, input().split()))
        if x[1] == x[3] and x[2] == x[4]:
            g = False
        if g:
            g = check(px, x)
        px = x
    if g:
        print('yes')
    else:
        print('no')
