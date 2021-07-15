def is_prime(num):

    # make sure n is a positive integer
    num = abs(int(num))

    # 0 and 1 are not primes
    if num < 2:
        return False

    # 2 is the only even prime number
    if num == 2: 
        return True    

    # all other even numbers are not primes
    if not num & 1: 
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False

    return True
