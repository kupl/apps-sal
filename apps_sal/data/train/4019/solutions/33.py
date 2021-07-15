def max_multiple(divisor, bound):
    for num in range(bound, 0,-1):
        print(num)
        if num % divisor == 0:
            return num

