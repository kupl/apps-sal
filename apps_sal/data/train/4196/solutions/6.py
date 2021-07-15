def summationOfPrimes(p):
    return sum([2]+[n for n in range(3,p+1,2) if all(n%i!=0 for i in range(2,n))])
