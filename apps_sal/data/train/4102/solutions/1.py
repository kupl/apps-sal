def odd_not_prime(n):
    return 1 + sum( any(not x%y for y in range(3,int(x**.5)+1,2)) for x in range(1,n+1,2))
