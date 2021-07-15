for T in range(int(input())):
    a, b, n = [int(x) for x in input().split()]

    if n % 3 == 0:
        print(a)
    elif n % 3 == 1:
        print(b)
    else:
        print(a ^ b)

