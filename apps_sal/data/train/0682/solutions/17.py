n = int(input())
l = list(map(int, input().split()))
f = 0
ans = 1
(l1, l2) = (0, 0)
for i in range(1, n + 1):
    if l[i - 1] != i:
        if f == 0:
            idx = l.index(i)
            k = l[0:i - 1] + l[i - 1:idx + 1][::-1] + l[idx + 1:]
            l = k
            f = 1
            l1 = i
            l2 = idx + 1
        else:
            ans = 0
if ans == 0:
    print(0, 0)
else:
    print(l1, l2)
