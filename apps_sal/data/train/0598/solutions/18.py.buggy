import sys
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
if k == 0:
    print(" ".join(map(str, a)))
elif k % 2 == 1:
    ma = max(a)
    print(" ".join(map(str, [ma - i for i in a])))
else:
    mi = min(a)
    print(" ".join(map(str, [i - mi for i in a])))
return
