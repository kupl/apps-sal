a = list(map(float, input().split()))
n = int(a[0])
j = 1
for i in range(n):
    x = a[j]
    y = a[j + 1]
    ans = x * 10 ** y
    print('{:.2f}'.format(ans))
    j += 2
