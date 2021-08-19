n = int(input())
aa = 0
mi = 10 ** 10
flag = True
for _ in range(n):
    (a, b) = [int(i) for i in input().split()]
    aa += a
    if a != b:
        flag = False
    if a > b:
        mi = min(mi, b)
if flag:
    print(0)
else:
    print(aa - (mi if mi != 10 ** 10 else 0))
