for _ in range(int(input())):
    (a, b, c) = list(map(int, input().split()))
    ma = max(a, b, c)
    mb = min(a, b, c)
    mc = a + b + c - ma - mb
    if ma <= mb + mc + 1:
        print('Yes')
    else:
        print('No')
