def primeFactors(n):
    ret,p,k="",2,0
    while (p<=n):
          while (n%p==0):
                n=n//p
                k+=1
          if (k):
              ret=ret+"("+str(p)+(("**"+str(k)) if k>1 else "")+")"
              k=0
          p+=1+(p>2)
    return(ret)
