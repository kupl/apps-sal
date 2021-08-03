n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
m1 = max(a)
m2 = min(a)
if k == 0:
    for i in a:
        print(i, end=' ')
elif k % 2 == 1:
    for i in a:
        print(m1 - i, end=' ')
else:
    for i in a:
        print(i - m2, end=' ')
