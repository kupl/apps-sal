def main():
    n = int(input())
    p = list([int(x) - 1 for x in input().split()])

    pos = [j for i, j in sorted([(j, i) for i, j in enumerate(p)])]
    basesize = n >> 1
    num = 1
    while num < basesize:
        num *= 2
    num -= 1

    tree_even = [100001] * (num * 2 + 1)
    tree_odd = [100001] * (num * 2 + 1)

    for i in range(num, num + basesize):
        tree_even[i] = p[(i - num) * 2]
    for i in range(num - 1, -1, -1):
        tree_even[i] = min(tree_even[2 * i + 1:2 * i + 3])
    for i in range(num, num + basesize):
        tree_odd[i] = p[(i - num) * 2 + 1]
    for i in range(num - 1, -1, -1):
        tree_odd[i] = min(tree_odd[2 * i + 1:2 * i + 3])

    g = dict()
    d = dict()
    q = [n - 1]
    qap, qp = q.append, q.pop
    while q:
        t = qp()
        m, M = t // n, t % n
        if m + 1 == M:
            d[t] = p[m] * n + p[M]
            continue
        g[t] = []
        gap = g[t].append
        if m % 2 == 0:
            i1, j1 = m >> 1, (M >> 1) + 1
            even = 200000
            l, r = i1 + num, j1 + num
            while l < r:
                if r % 2 == 0:
                    r -= 1
                    even = min(even, tree_even[r])
                if l % 2 == 0:
                    even = min(even, tree_even[l])
                    l += 1
                l >>= 1
                r >>= 1
            even_idx = pos[even]
            odd = 200000
            l, r = (even_idx >> 1) + num, j1 + num
            while l < r:
                if r % 2 == 0:
                    r -= 1
                    odd = min(odd, tree_odd[r])
                if l % 2 == 0:
                    odd = min(odd, tree_odd[l])
                    l += 1
                l >>= 1
                r >>= 1
            odd_idx = pos[odd]
            d[t] = even * n + odd
            if m != even_idx:
                s = m * n + even_idx - 1
                qap(s)
                gap(s)
            if M != odd_idx:
                s = (odd_idx + 1) * n + M
                qap(s)
                gap(s)
            if even_idx + 1 != odd_idx:
                s = (even_idx + 1) * n + odd_idx - 1
                qap(s)
                gap(s)
        else:
            i1, j1 = m >> 1, M >> 1
            odd = 200000
            l, r = i1 + num, j1 + num
            while l < r:
                if r % 2 == 0:
                    r -= 1
                    odd = min(odd, tree_odd[r])
                if l % 2 == 0:
                    odd = min(odd, tree_odd[l])
                    l += 1
                l >>= 1
                r >>= 1
            odd_idx = pos[odd]
            even = 200000
            l, r = (odd_idx >> 1) + 1 + num, j1 + 1 + num
            while l < r:
                if r % 2 == 0:
                    r -= 1
                    even = min(even, tree_even[r])
                if l % 2 == 0:
                    even = min(even, tree_even[l])
                    l += 1
                l >>= 1
                r >>= 1
            even_idx = pos[even]
            d[t] = odd * n + even
            if m != odd_idx:
                s = m * n + odd_idx - 1
                qap(s)
                gap(s)
            if M != even_idx:
                s = (even_idx + 1) * n + M
                qap(s)
                gap(s)
            if odd_idx + 1 != even_idx:
                s = (odd_idx + 1) * n + even_idx - 1
                qap(s)
                gap(s)

    g2 = dict()

    for i, t in list(g.items()):
        k = d[i]
        g2[k] = []
        ga = g2[k].append
        for j in t:
            ga(d[j])

    import heapq
    h = [d[n - 1]]
    heapq.heapify(h)
    ans = []
    hpop = heapq.heappop
    hpush = heapq.heappush

    while h:
        t = hpop(h)
        ans += [t // n + 1, t % n + 1]
        if t in g2:
            for s in g2[t]:
                hpush(h, s)

    print((*ans))


main()
