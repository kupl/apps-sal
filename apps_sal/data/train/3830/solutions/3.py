def chain_arith_deriv(start, k):
    res=[start]
    for i in range(k-1):
       s=0; r=factorize(start)
       if i==0 and r=={start:1}: return str(start)+" is a prime number"
       try:
          for n in r:
             p=1
             for n2 in r: p*= r[n2]*n2**(r[n2]-1) if n2==n else n2**r[n2]
             s+=p
          start=s; res.append(s)
       except: res.append(1)   
    return res

def factorize(num):
    if num<4: return [num]
    r={}; d=2
    while d<num**.5+1:
        while not num%d: 
           r[d]= r[d]+1 if d in r else 1
           num/=d
        d+=1 if d==2 else 2
    if num!=1: r[num]=1
    return r
