def res(n):
    l = len(n)
    maxx = max(n)
    i = 0
    i = n.index(maxx)
    if(i == 0 or i == l - 1):
        return 1
    else:
        return 1 + min(res(n[:i]), res(n[i + 1:]))


t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    l = list(map(int, input().split()))
    print(res(l))
