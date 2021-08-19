def reverse_factorial(num):
    i = 1
    while 1:
        (num, m) = (num / i, num % i)
        if m != 0:
            return 'None'
        if num == 1:
            return str(i) + '!'
        i += 1
