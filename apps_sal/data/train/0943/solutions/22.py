for _ in range(int(input())):
    a , b = list(map(int, input().split()))
    if b > a:
        b = a
    print(b + 1)

