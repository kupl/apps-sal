import string


def __starting_point():
    A = input()

    p = {}
    for x in string.ascii_lowercase:
        p[x] = len(A)
    '''
    tb
    1つ目：
    2つ目：アルファベット
    3つ目：
    '''
    tb = [(0, 0, 0)] * len(A)
    tb.append((1, 0, 0))
    tb.append((0, 0, 0))
    for i, x in reversed(list(enumerate(A))):
        p[x] = i
        tb[i] = min([(tb[p[c] + 1][0] + 1, c, p[c] + 1) for c in string.ascii_lowercase])
    i = 0
    ans = []
    while i < len(A):
        ans.append(tb[i][1])
        i = tb[i][2]

    print(("".join(ans)))


__starting_point()
