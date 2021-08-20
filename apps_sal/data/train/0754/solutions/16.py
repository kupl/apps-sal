t = int(input())
while t > 0:
    n = int(input())
    count = 0
    while n > 0:
        r = n % 10
        if r % 2 == 0:
            count = count + 1
            break
        else:
            n = n // 10
    if count == 0:
        print('0')
    else:
        print('1')
    t = t - 1
