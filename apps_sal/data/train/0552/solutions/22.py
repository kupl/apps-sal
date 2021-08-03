# cook your dish here
t = int(input())
for i in range(t):
    sum = 0
    sum1 = 0
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    k = min(k, n - k)
    for p in range(k):
        sum += l[p]
    for q in range(k, n):
        sum1 += l[q]

    print(abs(sum - sum1))
