fam = int(input())
(extra, req) = (0, 0)
for i in range(fam):
    (s, n, k, r) = list(map(int, input().split()))
    if r > 1:
        sm = k * (r ** n - 1) // (r - 1)
    else:
        sm = k * n
    if sm <= s:
        print('POSSIBLE', s - sm)
        extra += s - sm
    else:
        print('IMPOSSIBLE', abs(s - sm))
        req += abs(s - sm)
if extra >= req:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
