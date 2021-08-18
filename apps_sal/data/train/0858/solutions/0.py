t = int(input())
while t > 0:
    n = int(input())
    if n == 1:
        print(1)
    else:
        c, num = 1, 2
        while num < n:
            num *= 2
        if num == n:
            print(num)
        else:
            print(num // 2)
    t -= 1
