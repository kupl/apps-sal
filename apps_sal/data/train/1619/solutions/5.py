def decompose(n):
    # your code
    def fun(s,i):
      if s<0:return None
      if s==0:return []
      for j in range(i-1,0,-1):
        some = fun(s-j**2,j)
        if some!=None:
          return some+[j]

    return fun(n**2,n)
