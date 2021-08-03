
a = input()
ans = 0
n = len(a)
for j in range(n - 2):
    for i in range(j + 1, n - 1):
        for t in range(i + 1, n):
            if a[j] == 'Q' and a[i] == 'A' and a[t] == 'Q':
                ans += 1
print(ans)
