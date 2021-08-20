def main():
    (n, m) = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in [0] * m]
    n_hozon = n
    g = [set() for _ in [0] * n]
    [g[a - 1].add(b - 1) for (a, b) in ab]
    [g[b - 1].add(a - 1) for (a, b) in ab]
    s = set([i for i in range(n)])
    (a_list, b_list) = ([], [])
    while True:
        if m == n * (n - 1) // 2:
            break
        a = [-1, 10 ** 10]
        for i in s:
            l = len(g[i])
            if l < a[1]:
                a = [i, l]
        a = a[0]
        b = [-1, 10 ** 10]
        for i in s - g[a] - {a}:
            l = len(g[i])
            if l < b[1]:
                b = [i, l]
        b = b[0]
        (a_set, b_set) = ({a}, {b})
        s.remove(a)
        s.remove(b)
        n -= 2
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
            if flag_a == flag_b == False:
                print(-1)
                return
            elif flag_a == False or flag_b == False:
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
            n -= 1
        a_list.append(len(a_set))
        b_list.append(len(b_set))
    m = n
    n = n_hozon
    k = len(a_list)
    if k == 1:
        dp = [False] * (n + 1)
        a = a_list[0]
        b = b_list[0]
        ans = 10 ** 10
        for i in range(m + 1):
            ans = min(ans, (a + i) * (a + i - 1) // 2 + (n - a - i) * (n - a - i - 1) // 2)
        print(ans)
        return
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(k):
        (a, b) = (a_list[i], b_list[i])
        maxab = max(a, b)
        dp2 = [False] * (n + 1)
        for j in range(n - maxab + 1):
            dp2[j + a] |= dp[j]
            dp2[j + b] |= dp[j]
        dp = dp2
    dp2 = [False] * (n + 1)
    for j in range(m + 1):
        for i in range(n - j + 1):
            dp2[i + j] |= dp[i]
    ans = 10 ** 10
    for i in range(n + 1):
        if dp2[i] is False:
            continue
        j = n - i
        ans = min(ans, i * (i - 1) // 2 + j * (j - 1) // 2)
    print(ans)


main()
