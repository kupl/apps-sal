isprime=lambda x:x>1 and all(x%i for i in range(2,int(x**.5)+1))
goldbach=lambda n:[[i,n-i] for i in range(n // 2 + 1) if isprime(i) and isprime(n-i)] 
