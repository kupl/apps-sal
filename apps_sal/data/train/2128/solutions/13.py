n = input()
a = list(map(int, input().split(' ')))
n0 = a.count(0)
n1 = a.count(1)
res = list()
if n0 < n1:
    n1_cnt = 0
    for i in a:
        if i == 1:
            n1_cnt += 1
        else:
            res.append(n1_cnt)
else:
    n0_cnt = 0
    for i in reversed(a):
        if i == 0:
            n0_cnt += 1
        else:
            res.append(n0_cnt)
print(sum(res))
