n = int(input())
a = [x for x in input()]
b = [x for x in input()]
ans = 0
for i in range(n):
    if a[i] != b[i]:
        if i < n - 1:
            if a[i] == b[i + 1] and b[i] == a[i + 1]:
                a[i] = b[i]
                a[i + 1] = b[i + 1]
                ans += 1
for i in range(n):
    if a[i] != b[i]:
        ans += 1
print(ans)
