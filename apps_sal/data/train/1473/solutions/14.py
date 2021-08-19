def do_cut(r, c, m, k, j, mask):
    if mask == 0:
        if r == 0 or c == 0:
            return True
        else:
            return False
    if r <= 0 or c <= 0:
        return False
    cut_poss = False
    ans = False
    if m % r == 0 and mask & 4:
        ans = ans or do_cut(r, c - m / r, m, k, j, mask & 3)
        cut_poss = True
    if m % c == 0 and mask & 4:
        ans = ans or do_cut(r - m / c, c, m, k, j, mask & 3)
        cut_poss = True
    if k % r == 0 and mask & 2:
        ans = ans or do_cut(r, c - k / r, m, k, j, mask & 5)
        cut_poss = True
    if k % c == 0 and mask & 2:
        ans = ans or do_cut(r - k / c, c, m, k, j, mask & 5)
        cut_poss = True
    if j % r == 0 and mask & 1:
        ans = ans or do_cut(r, c - j / r, m, k, j, mask & 6)
        cut_poss = True
    if j % c == 0 and mask & 1:
        ans = ans or do_cut(r - j / c, c, m, k, j, mask & 6)
        cut_poss = True
    if not cut_poss:
        return False
    return ans


def solve():
    t = eval(input())
    while t > 0:
        (r, c, m, k, j) = list(map(int, input().split()))
        ans = do_cut(r, c, m, k, j, 7)
        print('Yes' if ans else 'No')
        t -= 1


solve()
