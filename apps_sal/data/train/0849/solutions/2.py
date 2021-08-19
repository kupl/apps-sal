n = int(input())
a = list(map(int, input().split()))
m = max(a)
ans = 0
i = 0
while i < n:
    temp = 0
    if a[i] == m:
        while i < n and a[i] == m:
            i += 1
            temp += 1
        ans = max(ans, temp)
    else:
        i += 1
print(ans)
