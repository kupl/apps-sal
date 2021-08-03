from itertools import permutations
k = []
d = []


def abc(l):
    ans = 0
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            ans += 1
    return ans


for i in range(8):
    k.append(i + 1)
    x = list(permutations(k))
    c = []
    for j in range(8):
        c.append([])
    d.append(c)
    for j in x:
        d[i][abc(j)].append(j)

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ans = 0
    c = d[n - 1][k]
    for i in c:
        flag = 1
        for j in range(n):
            if l[j] != 0 and l[j] != i[j]:
                flag = 0
                break
        if flag:
            ans += 1
    print(ans)
