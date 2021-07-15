is_prime_happy=lambda n:n>2and(2+sum(p*all(p%d for d in range(3,int(p**.5)+1,2))for p in range(3,n,2)))%n<1
