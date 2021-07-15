T = int(input())


def move_up(taken, s):
    s += 1
    while s in taken:
        s += 1
    return s


def move_down(taken, s):
    s -= 1
    while s in taken:
        s -= 1
    return s

for t in range(T):
    N, M = [int(_) for _ in input().split()]
    start = (1 << (M-1))-1
    taken = set()
    rd = True
    for i in range(N):
        el = int(input(), 2)
        taken.add(el)
        if el > start:
            if not rd:
                start = move_down(taken, start)
        elif el < start:
            if rd:
                start = move_up(taken, start)
        else:
            if rd:
                start = move_up(taken, start)
            else:
                start = move_down(taken, start)
        rd = not rd

    print(format(start, '0{}b'.format(M)))

