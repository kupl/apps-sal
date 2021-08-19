n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(key=lambda x: -x)
b.sort(key=lambda x: -x)
t = False
n1 = min(m, n)
if n > m:
    t = True
else:
    for i in range(n1):
        if a[i] > b[i]:
            t = True
if t:
    print('YES')
else:
    print('NO')


# Made By Mostafa_Khaled
