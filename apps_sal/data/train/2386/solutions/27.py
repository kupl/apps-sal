def solve():
    n = int(input())
    pp = list(map(int, input().split()))
    p = []
    e = set()
    for x in pp:
        if x not in e:
            p.append(x)
            e.add(x)
    print(*p)


for _ in range(int(input())):
    solve()
