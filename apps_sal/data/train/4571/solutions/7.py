def decompose(num):
  from math import log
  
  t = 2
  ks = []
  
  while (num**.5) >= t:
    k = int(log(num, t))
    num -= t**k
    ks.append(k)
    t += 1
  
  return [ks, num]
