modulo = int(1000000000.0) + 7
for t in range(int(input())):
    (l, r) = map(int, input().split())
    curr = 1
    ans = 0
    for i in range(61):
        q = l // curr
        if q & 1:
            end = min(r, (q + 1) * curr - 1)
            ans = (ans + curr * (end - l + 1) % modulo % modulo) % modulo
        curr *= 2
    print(ans)
