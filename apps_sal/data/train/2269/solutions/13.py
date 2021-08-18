

def main():
    from sys import stdin
    input = stdin.readline
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in [0] * m]

    rest = n
    g = [set() for _ in [0] * n]
    [g[a - 1].add(b - 1) for a, b in ab]
    [g[b - 1].add(a - 1) for a, b in ab]
    s = set([i for i in range(n)])

    a_list, b_list = [], []
    while True:
        if m == rest * (rest - 1) // 2:
            break
        a = [-1, 10**10]
        for i in s:
            length = len(g[i])
            if length < a[1]:
                a = [i, length]
        a = a[0]
        b = [-1, 10**10]
        for i in s - g[a] - {a}:
            length = len(g[i])
            if length < b[1]:
                b = [i, length]
        b = b[0]
        a_set, b_set = {a}, {b}
        s.remove(a)
        s.remove(b)
        rest -= 2
        remain = set()
        for i in s:
            flag_a = True
            for j in a_set:
                if j not in g[i]:
                    flag_a = False
                else:
                    g[i].remove(j)
                    g[j].remove(i)
                    m -= 1
            flag_b = True
            for j in b_set:
                if j not in g[i]:
                    flag_b = False
                else:
                    g[i].remove(j)
                    g[j].remove(i)
                    m -= 1
            if flag_a + flag_b == 0:
                print(-1)
                return
            elif flag_a * flag_b == 0:
                q = {i}
                flag = flag_a
                while q:
                    qq = set()
                    while q:
                        i = q.pop()
                        if flag:
                            a_set.add(i)
                        else:
                            b_set.add(i)
                        for j in remain:
                            if j not in g[i]:
                                qq.add(j)
                            else:
                                g[i].remove(j)
                                g[j].remove(i)
                                m -= 1
                        for j in q:
                            g[i].remove(j)
                            g[j].remove(i)
                            m -= 1
                    for i in qq:
                        remain.remove(i)
                    flag ^= True
                    q = qq
            else:
                remain.add(i)
        for i in (a_set | b_set) - {a} - {b}:
            s.remove(i)
            rest -= 1

        a_list.append(len(a_set))
        b_list.append(len(b_set))

    k = len(a_list)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(k):
        a, b = a_list[i], b_list[i]
        dp2 = [False] * (n + 1)
        for j in range(n - max(a, b) + 1):
            dp2[j + a] |= dp[j]
            dp2[j + b] |= dp[j]
        dp = dp2

    ans = 10**10
    for j in range(rest + 1):
        for i in range(n - j + 1):
            if dp[i]:
                p = i + j
                q = n - p
                ans = min(ans, p * (p - 1) // 2 + q * (q - 1) // 2)
    print(ans)


main()
