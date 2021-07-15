n = int(input())
a = list(input())
b = list(input())

ans = 0
i = 0
while i < n:
    if a[i] != b[i]:
        ans += 1
        if i < n - 1 and a[i] == b[i + 1] and b[i] == a[i + 1]:
            i += 1
    i += 1
print(ans)

