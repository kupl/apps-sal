try:
    for i in range(int(input())):
        n = int(input())
        ai = list(map(int, input().split()))
        bi = list(map(int, input().split()))
        sa = 0
        sb = 0
        ans = 0
        for i in range(0, n):
            if ai[i] == bi[i]:
                if sum(ai[:i]) == sum(bi[:i]):
                    ans = ans + ai[i]
                else:
                    sa = sa + ai[i]
                    sb = sb + bi[i]
            else:
                sa = sa + ai[i]
                sb = sb + bi[i]
        print(ans)
except:
    pass
