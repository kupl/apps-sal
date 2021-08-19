# cook your dish here# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = [0 for i in range(n)]
    for i in range(n):
        m[a[i]] = a[i]
    print(*m)
