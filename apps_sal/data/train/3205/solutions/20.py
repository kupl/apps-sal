def is_divisible(n, x, y):
    if n > 0 and x > 0 and y > 0:
        if n % x == 0 and n % y == 0:
            print("Target number IS divisible by BOTH divisors")
            return True
        else:
            print("Target number is NOT divisible by BOTH devisors")
            return False
    else:
        print("Incorrect input: One or more arguments are not higher than zero")
