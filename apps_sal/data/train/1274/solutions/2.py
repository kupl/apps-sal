for _ in range(int(input())):
    n = int(input())
    b = 1
    # 1112
    # 2122
    for _ in range(1, n + 1):
        a = 1
        for __ in range((2 * n)):
            if __ % 2 == 0:
                print(a, end="")
                a += 1
            else:
                print(b, end="")
        b += 1
        print()
    print()
