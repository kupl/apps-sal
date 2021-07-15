def zeroes (b, n):
  d1={} #for decomposition of base into power of primefactors
  i=2
  while b>1:
    while b%i==0:
      try:
        d1[i]+=1
      except KeyError:
        d1[i]=1
      b//=i
    i+=1
  d2={} #for total powers of the primefactors in the number
  for i in d1:
    s=0
    r=i
    while r<=n:
      s+=n//r
      r*=i
    d2[i]=s
  return min(list(d2[i]//d1[i] for i in d1))

