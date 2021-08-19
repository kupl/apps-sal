def is_divisible(n, x, y):
    # your code here
    while n != 0:
        if n % x == 0 and n % y == 0:
            return True
        else:
            return False
