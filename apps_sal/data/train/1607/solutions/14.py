s = list(input())
n = len(s)

ans = 0
for i in range(n - 2):
    if s[i] != 'Q':
        continue
    for j in range(i + 1, n - 1):
        if s[j] != 'A':
            continue
        for k in range(j + 1, n):
            if s[k] != 'Q':
                continue
            ans += 1
print(ans)

