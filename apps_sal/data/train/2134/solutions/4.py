n = int(input())
p = [1] + list(map(int, input().split()))
s = list(map(int, input().split()))
p = [i - 1 for i in p]
for i in range(1, n):
    if s[i] != -1 and (s[p[i]] == -1 or s[p[i]] > s[i]):
        s[p[i]] = s[i]
a = [s[0]] + [0] * (n - 1)
for i in range(1, n):
    if s[i] == -1:
        a[i] = 0
    else:
        a[i] = s[i] - s[p[i]]
        if a[i] < 0:
            print(-1)
            quit()
print(sum(a))
