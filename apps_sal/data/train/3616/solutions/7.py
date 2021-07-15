def prime_primes(N):
    prime = []
    for iter in range(2,N):
        for i in range(2,iter):
             if (iter%i)==0:
               break
        else:
               prime.append(iter)
    
    l = [j/i for i in prime for j in prime if (j/i)<1]
    return (len(l),int(sum(l)))
