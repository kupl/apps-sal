n, m, k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

ans = 'NO'

if n > m:
    ans = 'YES'
else:
    for i in range(n):
        if a[i] > b[i]:
            ans = 'YES'

print(ans)
