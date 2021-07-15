def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(31, -1, -1):
        k = 1 << i
        u, v = 0, 0
        for j in a:
            if j & k:
                u += 1
            else:
                v += 1
        if v % 2 == 1:
            if u % 2 == 1:
                print('WIN')
                return
        else:
            if u % 4 == 1:
                print('WIN')
                return
            elif u % 4 == 3:
                print('LOSE')
                return
    print('DRAW')

t = int(input())
for _ in range(t):
    solve()
