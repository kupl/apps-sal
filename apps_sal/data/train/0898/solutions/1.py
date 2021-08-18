def sol(z):
    r = len(str(z))
    if(z < int(str(9) * r)):
        r -= 1
    return r


t = int(input())
for _ in range(t):
    i, j = map(int, input().split())
    l = i
    print(l * sol(j), l)
