def divisors(n):
    '''
        Returns the number of divisors of a positive integer
        ~Input: 
            n, the given integer
        ~Output:
            x, the number of divisors
    '''
    x = 0
    for i in range(1, n+1):
        if n % i == 0:
            x += 1
    
    return x
