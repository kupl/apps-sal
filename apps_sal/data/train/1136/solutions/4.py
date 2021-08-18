for i in range(int(input())):
    n, k = list(map(int, input().split()))
    d = n // 2
    if(n % 2 == 1):
        d += 1
    print(d * k)
