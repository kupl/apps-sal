t = int(input())
for i in range(t):
    (n, k, d) = map(int, input().split())
    if n == 1:
        summ = int(input())
    else:
        a = []
        a = list(map(int, input().strip().split()))[:n]
        summ = sum(a)
    tot = summ // k
    print(min(d, tot))
