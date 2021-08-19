for _ in range(int(input())):
    ans = 0
    (n, k) = map(int, input().split())
    dic = {}
    for _ in range(n):
        (s, f, p) = map(int, input().split())
        if p not in dic:
            dic[p] = [(s, f)]
        else:
            dic[p].append((s, f))
    for (key, val) in dic.items():
        if len(dic[key]) > 1:
            x = 0
            for dekho in sorted(dic[key], key=lambda x: x[1]):
                if dekho[0] >= x:
                    ans += 1
                    x = dekho[1]
        else:
            ans += 1
    print(ans)
