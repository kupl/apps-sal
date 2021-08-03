def solve():
    n = int(input())
    l = []
    l = list(map(int, input().split()))
    l.sort()
    c = 0
    if(l[0] == 0):
        c = 1
    for i in range(1, len(l)):
        if l[i] <= c:
            c += 1
    print(c)


t = int(input())
i = 0
while i < t:
    solve()
    i += 1
