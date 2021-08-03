def hotpo(n):
    x = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        x += 1
    return x

# if(number is even) number = number / 2
# if(number is odd) number = 3*number + 1
