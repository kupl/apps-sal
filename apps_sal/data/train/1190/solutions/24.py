for i in range(int(input())):
    a = int(input())
    j = 11
    c = 0
    while a > 0:
        b = a // 2 ** j
        c += b
        a = a % 2 ** j
        j -= 1
    print(c)
