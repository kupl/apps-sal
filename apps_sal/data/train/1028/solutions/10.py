for nt in range(int(input())):
    num = int(input())
    sum = 0
    temp = num
    r = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** r
        temp //= 10
    if num == sum:
        print('FEELS GOOD')
    else:
        print('FEELS BAD')
