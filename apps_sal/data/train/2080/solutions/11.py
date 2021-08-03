m = int(input())
dis = list(map(int, input().split()))
n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=True)
dis.sort()
money = sum(p)
mind = dis[0]
if n <= mind:
    print(sum(p))
else:
    i = mind - 1
    while i < n:
        if i + 1 < n:
            money -= p[i + 1]
        if i + 2 < n:
            money -= p[i + 2]
        i += mind + 2
    print(money)
