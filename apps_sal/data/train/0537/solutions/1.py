n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
i = 0
s = 0
for j in range(0, n):
    while(i < n):
        if(a[i] - a[j] >= k):
            s = s + (n - i)
            break
        i = i + 1
print(s)
