n, l = map(int, input().split( ))
t = list()
for i in range(n):
    s = input()
    t.append(s)
t.sort()
ans = ""
for j in range(n):
    ans += t[j]
print(ans)
