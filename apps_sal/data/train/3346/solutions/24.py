def gap(g, m, n):
        x = [n]
        for i in range(m,n+1):
                        if check_prime(i):
                             x.append(i)
                             if len(x)>=2 and x[len(x)-1]-x[len(x)-2]==g:
                                         return [x[len(x)-2],x[len(x)-1]]
                             else:
                                  x.remove(x[len(x)-2])


def check_prime(i):
     for j in range(2,int(i**0.5 +1)):
            if i%j==0:
                 return False
     return True
