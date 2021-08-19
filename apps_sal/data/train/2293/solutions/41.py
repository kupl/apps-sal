N = int(input())
A = list(map(int, input().split()))
dp1 = [(0, A[0])]
ans = 0
for i in range(1, 1 << N):
    d = {i: A[i]}
    for k in range(18):
        b = 1 << k
        if i & b == 0:
            continue
        (j, v) = dp1[i - b]
        d.update({j: v})
    (p1, p2) = sorted(list(d.items()), key=lambda x: -x[1])[:2]
    dp1.append(p1)
    ans = max(ans, p1[1] + p2[1])
    print(ans)
