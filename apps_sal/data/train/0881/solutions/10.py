# cook your dish here
t = int(input())
for ts in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = [1] * n
    for i in range(n - 1):
        if l[i] <= l[i + 1]:
            m[i + 1] = m[i] + 1
    print(sum(m))
