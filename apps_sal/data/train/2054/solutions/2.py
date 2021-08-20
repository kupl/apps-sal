n = int(input())
e = [list(map(int, input().split())) for i in range(n - 1)]
c = list(map(int, input().split()))
(ec, v) = ([0] * n, 0)
for (ea, eb) in e:
    if c[ea - 1] != c[eb - 1]:
        ec[ea - 1] += 1
        ec[eb - 1] += 1
        v += 1
if v == max(ec):
    print('YES', ec.index(v) + 1, sep='\n')
else:
    print('NO')
