

def can_cut_h(r, c, s1, s2):
    if (s1 % r != 0) and (s2 % r != 0):
        return None
    c1, c2 = s1 / r, s2 / r
    if c1 + c2 != c:
        return None

    return c2


def can_cut_v(r, c, s1, s2):
    if (s1 % c != 0) and (s2 % c != 0):
        return None
    r1, r2 = s1 / c, s2 / c
    if r1 + r2 != r:
        return None

    return r2


def solve(r, c, m, k, j):
    if (m + k + j) != r * c:
        return "No",
    in_order = [m, k, j]
    for _ in range(3):
        s1 = in_order.pop()
        s2, s3 = in_order
        in_order.insert(0, s1)
        v_r = can_cut_v(r, c, s1, s2 + s3)
        h_c = can_cut_h(r, c, s1, s2 + s3)
        if v_r is not None:
            if can_cut_h(v_r, c, s2, s3) or can_cut_v(v_r, c, s2, s3):
                return "Yes",
        if h_c is not None:
            if can_cut_h(r, h_c, s2, s3) or can_cut_v(r, h_c, s2, s3):
                return "Yes",
    return "No",


def read_input():
    r, c, m, k, j = list(map(int, input().split()))
    return r, c, m, k, j


def __starting_point():
    t = int(input())
    for i in range(t):
        res = list(map(str, solve(*read_input())))
        print(" ".join(res))
    # print solve(4, 5, 10, 4, 6)
    # print solve(4, 5, 6, 10, 4)
    # print solve(4, 5, 4, 6, 10)
    # print solve(2, 2, 2, 2, 2)


__starting_point()
