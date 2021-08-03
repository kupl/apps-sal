# cook your dish here
try:
    n, k = map(int, input().split())
    l = []
    for i in range(n):
        h = int(input())
        l.append(h)
    l.sort()
    mn = max(l)
    for i in range(n - k):
        mn = min(mn, l[i + k - 1] - l[i])
    print(mn)


except:
    pass
