n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if n > m:
    print('YES')
else:
    a.sort()
    b.sort()
    b = b[-n:]
    ans = 'NO'
    for i in range(n):
        if a[i] > b[i]:
            ans = 'YES'
    print(ans)
