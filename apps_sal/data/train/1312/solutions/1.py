def check(L):
    for l in L:
        if 'spoon' in ''.join(l):
            return True
    return False


def change(r, c, L):
    n = []
    for x in range(c):
        t = []
        for q in range(r):
            t.append(L[q][x])
        n.append(t)
    return n


for case in range(eval(input())):
    (r, c) = list(map(int, input().strip().split()))
    m = []
    for row in range(r):
        m.append(list(input().lower().strip()))
    if check(m):
        print('There is a spoon!')
    else:
        m = change(r, c, m)
        if check(m):
            print('There is a spoon!')
        else:
            print('There is indeed no spoon!')
