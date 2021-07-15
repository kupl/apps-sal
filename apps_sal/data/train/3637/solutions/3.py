def num_primorial(n):
    """
    Custom Sieve method used...
    """
    prime_list = [2]
    ans = prime_list[0]
    chk_num = 3
    while len(prime_list) != n:
        for prime in prime_list:
            if chk_num % prime == 0:
               break
            elif prime == prime_list[-1]: # and chk_num%prime != 0
                prime_list.append(chk_num)   # chk_num is prime
                ans = ans*prime_list[-1] # update answer
        chk_num = chk_num + 2 #all primes after 2 are odd
    return ans


