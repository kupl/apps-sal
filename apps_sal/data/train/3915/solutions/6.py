def ss(n): return sum(map(int, str(n)))


def solve(s):
    s = s.split('\n')
    ans = []
    for i in s:
        j, k = map(int, i.split())
        c = (-ss(j + k) + ss(k) + ss(j)) // 9
        cc = "No" if c == 0 else str(c)
        ans.append(cc + ' carry operation' + 's' * (c > 0))
    return '\n'.join(ans)
