t = int(input())
while t:
    (n, k, v) = map(int, input().split(' '))
    lst = list(map(int, input().split(' ')))
    tot = sum(lst)
    x = (v * (n + k) - tot) / k
    if int(x) == x and x > 0:
        print(int(x))
    else:
        print(-1)
    t = t - 1
