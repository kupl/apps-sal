for case in range(int(input())):
    n = int(input())
    while n % 7 != 0 and n >= 0:
        n -= 4
    if n < 0:
        print(-1)
    else:
        print(n)
