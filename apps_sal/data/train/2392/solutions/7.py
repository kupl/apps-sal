for q in range(int(input())):
    n, m = list(map(int, input().split()))
    if m % 10 == 0:
        print(0)
    elif m % 10 == 5:
        print((n//m+1)//2*5)
    elif m % 2 == 0:
        x = n//(m*5)*m*5
        ans = n//(m*5)*20
        while x <= n:
            ans += x % 10
            x += m
        print(ans)
    else:
        x = n // (m * 10) * m * 10
        ans = n // (m * 10)*45
        while x <= n:
            ans += x % 10
            x += m
        print(ans)

