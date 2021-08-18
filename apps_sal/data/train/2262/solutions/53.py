

def add(bound, r, c, x, y, i):
    if x == 0:
        bound.append((0, y, i))
    elif y == c:
        bound.append((1, x, i))
    elif x == r:
        bound.append((2, c - y, i))
    else:
        bound.append((3, r - x, i))


def solve(bound):

    if not bound:
        return True

    bound.sort()
    st = [0] * len(bound)
    p = -1

    for _, _, i in bound:
        if 0 <= p and st[p] == i:
            p -= 1
        else:
            p += 1
            st[p] = i

    return p == -1


def main():
    r, c, n = input().split()
    r = int(r)
    c = int(c)
    n = int(n)
    bound = []
    for i in range(n):
        x1, y1, x2, y2 = input().split()
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if (x1 % r == 0 or y1 % c == 0) and (x2 % r == 0 or y2 % c == 0):
            add(bound, r, c, x1, y1, i)
            add(bound, r, c, x2, y2, i)

    print(('YES' if solve(bound) else 'NO'))


def __starting_point():
    main()


__starting_point()
