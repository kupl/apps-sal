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


def t_diff(h, m):
    max_t_diff = None
    for i in range(len(h) - 1):
        (h_diff, m_diff) = (h[i] - h[i + 1], m[i] - m[i + 1])
        if h_diff == m_diff or m_diff == 0:
            continue
        if h_diff == 0:
            return 1
        if (h_diff < 0) != (m_diff < 0):
            local_t_diff = max(1, abs(h_diff / m_diff))
            if max_t_diff is None:
                max_t_diff = local_t_diff
            else:
                max_t_diff = min(max_t_diff, local_t_diff)
    return max_t_diff


def no_more_changes(h, m):
    for i in range(len(h) - 1):
        (h_diff, m_diff) = (h[i] - h[i + 1], m[i] - m[i + 1])
        if h_diff == m_diff or m_diff == 0:
            continue
        if h_diff == 0 or (h_diff < 0) != (m_diff < 0):
            return False
    return True


for _ in range(eval(input())):
    n = eval(input())
    (h, m) = list(map(list, list(zip(*[list(map(int, input().split())) for _ in range(n)]))))
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
        td = t_diff(h, m)
        if td is None:
            if zig_zag_start is not None:
                zig_zags.append((zig_zag_start, 'Inf'))
                zig_zag_start = None
            break
        h = list(map(lambda x, y: x + td * y, h, m))
        t += td
    print(len(zig_zags))
    for (s, e) in zig_zags:
        print(s, e)
