for _ in range(int(input())):
    n, w = map(int, input().split())
    sigma = 1
    if(w > 9 or w < -9):
        print(0)
        continue
    sigma = pow(10, n - 2, 1000000007)
    if(w >= 0):
        sigma *= (9 - w)
    else:
        sigma *= (w + 10)
    print(sigma % 1000000007)
