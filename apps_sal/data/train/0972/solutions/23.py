n, k = list(map(int, input().split(" ")))
l = []
for i in range(n):
    a = int(input())
    l.append(a)
l.sort()
mini = 10**10
for i in range(n - k + 1):
    mini = min(mini, l[i + k - 1] - l[i])
print(mini)
