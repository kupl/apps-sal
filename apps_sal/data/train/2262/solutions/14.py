def calc_pos(x, y, R, C):
    if y == 0:
        return x
    if y == C:
        return 2 * R + C - x
    if x == R:
        return R + y
    if x == 0:
        return 2 * R + 2 * C - y


def read_data():
    (R, C, N) = list(map(int, input().split()))
    pairs = []
    xys = []
    idx = 0
    for i in range(N):
        (x1, y1, x2, y2) = list(map(int, input().split()))
        xys.append((x1, y1))
        xys.append((x2, y2))
        if x1 != 0 and x1 != R and (y1 != 0) and (y1 != C) or (x2 != 0 and x2 != R and (y2 != 0) and (y2 != C)):
            continue
        a = calc_pos(x1, y1, R, C)
        b = calc_pos(x2, y2, R, C)
        pairs.append((a, idx))
        pairs.append((b, idx))
        idx += 1
    pairs.sort()
    return (pairs, xys)


def is_valid(xys):
    xys.sort()
    (prev_x, prev_y) = xys[0]
    for (x, y) in xys[1:]:
        if prev_x == x and prev_y == y:
            return False
        prev_x = x
        prev_y = y
    return True


def solve(pairs, xys):
    if len(xys) == 2:
        return 'YES'
    if not is_valid(xys):
        return 'NO'
    idxs = [i for (a, i) in pairs]
    stack = []
    for idx in idxs:
        if stack and stack[-1] == idx:
            stack.pop()
            continue
        stack.append(idx)
    if stack:
        return 'NO'
    else:
        return 'YES'


(pairs, xys) = read_data()
print(solve(pairs, xys))
