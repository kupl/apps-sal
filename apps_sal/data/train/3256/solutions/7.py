def sum_pow_dig_seq(start, n, k):
    r=[]
    for i in range (0,k):
       c=0
       for d in str(start):
          c+=int(d)**n
       r.append(c); start=c
    for i in range (0,k):
       if r[i] in r[i+1:]:
          posE=r.index(r[i],i+1)
          if posE>=0:
             if r[i:posE-1]==r[posE:posE+posE-1-i]: posS=i; break 
    return [posS+1, r[posS:posE], posE-posS, start]
