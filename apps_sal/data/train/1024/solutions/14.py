poss = 0
imposs = 0
for _ in range(int(input())):
    (s, n, k, r) = list(map(int, input().split()))
    a = [0] * n
    a[0] = k
    for i in range(1, n):
        a[i] = a[i - 1] * r
    if sum(a) <= s:
        x = s - sum(a)
        print('POSSIBLE ' + str(x))
        poss = poss + x
    else:
        y = abs(s - sum(a))
        print('IMPOSSIBLE ' + str(y))
        imposs = imposs + y
if imposs <= poss:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
