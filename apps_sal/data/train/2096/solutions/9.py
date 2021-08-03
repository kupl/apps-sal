n = int(input())
a = list(map(int, input().split()))
s = [(a[i], i) for i in range(n)]
s.sort()
x = [-1] * n
for i in range(n):
    x[s[i][1]] = i
ans = []
for i in range(n):
    if x[i] != -1:
        j = i
        q = []
        while x[j] != -1:
            q.append(str(j + 1))
            t = j
            j = x[j]
            x[t] = -1
        ans.append(str(len(q)) + ' ' + ' '.join(q))
print(len(ans))
print(*ans, sep='\n')
