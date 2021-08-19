s = str(input())
n = len(s)
cnt = 0
for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if s[i] == 'Q' and s[j] == 'A' and (s[k] == 'Q'):
                cnt = cnt + 1
print(cnt)
