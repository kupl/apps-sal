t = int(input())
while t > 0:
    t -= 1
    n, tt = map(int, input().split())
    l = list(map(int, input().split()))
    while tt > 0:
        a, b = map(int, input().split())
        print(sum(l[a - 1:b]))
        tt -= 1
