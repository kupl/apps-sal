def is_zig_zag(h):
    if len(h) < 2:
        return True
    if h[0] == h[1]:
        return False
    fs = (lambda x, y: x < y, lambda x, y: x > y)
    f = 0 if h[0] < h[1] else 1
    for i in range(1, len(h) - 1):
        if not fs[(i + f) % 2](h[i], h[i + 1]):
            return False
    return True


def no_more_changes(h, m):
    for i in range(len(h) - 1):
        h_diff, m_diff = h[i] - h[i + 1], m[i] - m[i + 1]
        if h_diff == m_diff or m_diff == 0:
            continue
        if h_diff == 0 or (h_diff < 0) != (m_diff < 0):
            return False
    return True


for _ in range(eval(input())):
    n = eval(input())
    h, m = list(map(list, list(zip(*[list(map(int, input().split())) for _ in range(n)]))))
    t = 0
    zig_zags = []
    zig_zag_start = None
    while True:
        if is_zig_zag(h):
            if zig_zag_start is None:
                zig_zag_start = t
        elif zig_zag_start is not None:
            zig_zags.append((zig_zag_start, t - 1))
            zig_zag_start = None
        if no_more_changes(h, m):
            if zig_zag_start is not None:
                zig_zags.append((zig_zag_start, 'Inf'))
                zig_zag_start = None
            break
        h = list(map(lambda x, y: x + y, h, m))
        t += 1
    print(len(zig_zags))
    for s, e in zig_zags:
        print(s, e)
