# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    for i in range(n // 2):
        s += abs(a[n - i - 1] - a[i])
    print(s)
