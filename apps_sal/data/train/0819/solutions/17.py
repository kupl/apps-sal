for _ in range(int(input())):
    a, b = list(map(int, input().split()))

    flag = 0
    while 1:
        if a == b and a != 1:
            print("NO")
            flag = 1
            break

        elif a == 1 or b == 1:
            print("YES")
            flag = 1
            break

        elif a > b and a % b == 0:
            print("NO")
            flag = 1
            break

        elif b > a and b % a == 0:
            print("NO")
            flag = 1
            break

        if a > b:
            a, b = a % b, b
        else:
            a, b = a, b % a
