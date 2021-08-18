try:
    for i in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        sa = 0
        sb = 0
        ans = 0

        for i in range(0, n):
            sa = sa + a[i]
            sb = sb + b[i]
            if sa == sb and a[i] == b[i]:
                ans = ans + a[i]

        print(ans)
except:
    pass
