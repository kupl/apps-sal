count_divisors=lambda n:2*sum(n//i for i in range(1,int(n**.5)+1))-int(n**.5)**2
