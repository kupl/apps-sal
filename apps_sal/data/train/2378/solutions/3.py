
def main():
    buf = input()
    q = int(buf)
    s = []
    n = []
    for t in range(q):
        buf = input()
        s.append(buf)
        n.append(len(s[t]))

    ans = []
    for t in range(q):
        c = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        for i in range(n[t]):
            c[s[t][i]] += 1
        lr_min = min(c['L'], c['R'])
        ud_min = min(c['U'], c['D'])
        if lr_min == 0 and ud_min > 1:
            ud_min = 1
        if ud_min == 0 and lr_min > 1:
            lr_min = 1
        c['L'] = lr_min
        c['R'] = lr_min
        c['U'] = ud_min
        c['D'] = ud_min
        move = ''
        move += 'L' * lr_min
        move += 'U' * ud_min
        move += 'R' * lr_min
        move += 'D' * ud_min
        ans.append(move)
    for t in range(q):
        print(len(ans[t]))
        print(ans[t])


def __starting_point():
    main()


__starting_point()
