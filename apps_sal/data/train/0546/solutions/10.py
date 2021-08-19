for i in range(int(input())):
    a = int(input())
    sum = 0
    x = 2
    while a // x != 0:
        sum += 1
        x *= 2
    temp = 0
    while a >= 0 and sum >= 0:
        if 2 ** sum <= a:
            a -= 2 ** sum
            temp += 1
        sum -= 1
    print(temp - 1)
