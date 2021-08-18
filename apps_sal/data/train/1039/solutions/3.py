for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if a == b:
        print(0)
    else:
        if b > a:
            c = b - a
            if c % 2 != 0:
                print(1)
            else:
                c = c // 2
                if c % 2 == 0:
                    print(3)
                else:
                    print(2)
        else:
            c = a - b
            if c % 2 != 0:
                print(2)
            else:
                print(1)
