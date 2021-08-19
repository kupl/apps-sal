import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10 ** 9))


def write(x):
    return sys.stdout.write(x + '\n')


_turnx = {1: 4, 2: 3, 3: 2, 4: 1}
_turn90 = {1: 4, 2: 3, 3: 1, 4: 2}


def subx(a, b, d):
    if isinstance(a, tuple):
        return min((subx(item, b, d) for item in a))
    if d < 0:
        return subx(_turnx[a], _turnx[b], -d)
    return suby(_turn90[a], _turn90[b], d)


_turny = {1: 3, 2: 4, 3: 1, 4: 2}


def suby(a, b, d):
    if isinstance(a, tuple):
        return min((suby(item, b, d) for item in a))
    if d < 0:
        return suby(_turny[a], _turny[b], -d)
    elif d == 0:
        if a == b:
            return 0
        else:
            return 1
    elif d == 1:
        if a in (2, 3) and b in (1, 4):
            return 1
        elif a in (1, 4) and b in (2, 3):
            return 3
        else:
            return 2
    else:
        ans = 2 * (d - 2)
        if a in (1, 4):
            ans += 3
        else:
            ans += 2
        if b in (1, 4):
            ans += 1
        else:
            ans += 2
    return ans


ans = float('inf')
t = int(input())
for ind in range(t):
    (ax, ay, bx, by, cx, cy) = list(map(int, input().split()))
    if ax != bx:
        if bx == cx:
            (ax, ay, cx, cy) = (cx, cy, ax, ay)
        else:
            (bx, by, cx, cy) = (cx, cy, bx, by)
    if cx > ax:
        if cy == max(ay, by):
            k = 3
        else:
            k = 1
    elif cy == max(ay, by):
        k = 2
    else:
        k = 4
    (tx, ty) = (min(ax, bx, cx), min(ay, by, cy))
    if tx == 0:
        if ty == 0:
            ans = suby(1, k, 0)
        else:
            ans = suby(1, k, ty)
    elif ty == 0:
        ans = subx(1, k, tx)
    elif tx > 0 and ty > 0:
        ans = 2 * min(tx, ty) + 1
        if tx > ty:
            ans += subx((1, 3, 4), k, tx - ty)
        elif ty > tx:
            ans += suby((1, 3, 4), k, ty - tx)
        else:
            ans += suby((1, 3, 4), k, 0)
    elif tx > 0 and ty < 0:
        (tx, ty) = (abs(tx), abs(ty))
        ans = 2 * min(tx, ty)
        if tx > ty:
            ans += subx((1, 3), k, tx - ty)
        elif ty > tx:
            ans += suby((1, 3), k, tx - ty)
        else:
            ans += suby((1, 3), k, 0)
    elif tx < 0 and ty > 0:
        (tx, ty) = (abs(tx), abs(ty))
        ans = 2 * min(tx, ty)
        if tx > ty:
            ans += subx((1, 4), k, -tx + ty)
        elif ty > tx:
            ans += suby((1, 4), k, -tx + ty)
        else:
            ans += suby((1, 4), k, 0)
    else:
        (tx, ty) = (abs(tx), abs(ty))
        ans = 2 * min(tx, ty)
        if tx > ty:
            ans += subx((2, 3, 4), k, ty - tx)
        elif ty > tx:
            ans += suby((2, 3, 4), k, tx - ty)
        else:
            ans += suby((2, 3, 4), k, 0)
    print(ans)
