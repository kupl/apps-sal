def fun(l, n, i):
    ans = 0
    no_term = n - i + 1 + i // 2
    side = i + (no_term - 1)
    if side > n:
        side = 2 * (side - n) - 1
    count = 0
    power = 1
    if i % 2 == 0:
        ans += l[side - 1]
    while(side != i):
        if no_term % 2 == 0:
            no_term = no_term // 2
            # count+=1
            power *= 2
        else:
            no_term = (no_term // 2) + 1
            ans += l[side - 1]
            # count+=1
            power *= 2

        side = i + (no_term - 1) * power
        if side > n:
            side = 2 * (side - n) - 1
    return ans


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    f = int(input())
    ans = []
    c = 0
    count = 0
    P = None
    for i in range(len(l)):
        if l[i] <= f:
            c = 1
            if count == 0:
                count += 1
                D = fun(l, n - 1, i + 1)
                P = i + 1
            else:
                yt = fun(l, n - 1, i + 1)
                if yt < D:
                    P = i + 1
                    D = yt
    if c == 0:
        print('impossible')
    else:
        print('possible')
        print(P, D + f)
