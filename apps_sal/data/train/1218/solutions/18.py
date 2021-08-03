for _ in range(int(input())):
    a, b = [int(j) for j in input().split()]
    k = b // a
    if b % a != 0:
        print(a * ((k * (k + 1)) // 2))
    else:
        print(a * ((k * (k - 1)) // 2))
