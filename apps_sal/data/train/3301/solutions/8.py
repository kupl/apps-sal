def even_fib(m):
    s=0
    a,b=1,1
    while a<m:
      if a%2==0:
        s+=a
      a,b=b,a+b
    return s
