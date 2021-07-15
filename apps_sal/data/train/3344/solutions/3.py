def number_property(n):
    ans=[False,False,False]
    j=[]
    k=[]
    if n>1:
     for x in range(2,int(n ** 0.5)+ 1):
      j.append(x)
      if n%x:
        k.append(x)
     if k==j:
      ans[0]=True
    if n%2==0:
      ans[1]=True
    if n%10==0:
      ans[2]=True
    return ans
