x = input()
n = len(x)

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if x[i] == 'Q' and x[j] == 'A' and x[k] == 'Q':
                ans += 1

print(ans)
