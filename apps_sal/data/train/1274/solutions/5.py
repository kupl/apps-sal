import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append([str(i + 1)] * n)
        l = []
        for k in range(1, n + 1):
            l.append(str(k))
        a.append(l)
    ans = []
    for i in range(n):
        v = []
        for j in range(len(a)):
            v.append(a[j][i])
        ans.append(v)
    for ele in ans:
        print(''.join(ele))
