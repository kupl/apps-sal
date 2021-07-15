from math import gcd as builtin_gcd
 
"""
This problem could be seen as finding the Frobenius number
Algorithm used
https://brg.a2hosted.com/?page_id=563
based on
The Money Changing Problem Revisited: Computing the Frobenius Number in Time O(ka1), by Sebastian Bocker and Zsuzsanna Liptak, June 2004, Technical Report number 2004-2, University of Bielefeld, Technical Faculty.

"""    
    
def gcd(a, *r):
  for b in r:
    a = builtin_gcd(a, b)
  return a
 
def lcm(a, *r):
  for b in r:
    a *= b // builtin_gcd(a, b)
  return abs(a)
 
def frobenius_number(a):
  def __residue_table(a):
    n = [0] + [None] * (a[0] - 1)
    for i in range(1, len(a)):
      d = gcd(a[0], a[i])
      for r in range(d):
        try:
          nn = min(n[q] for q in range(r, a[0], d) if n[q] is not None)
        except ValueError:
          continue
        if nn is not None:
          for c in range(a[0] // d):
            nn += a[i]
            p = nn % a[0]
            nn = min(nn, n[p]) if n[p] is not None else nn
            n[p] = nn
    return n
 
  
  if len(a) < 2 or gcd(*a) > 1:
    return -1
  return max(__residue_table(sorted(a))) - min(a)

def min_price(a):
    if 1 in a:
        return 1
    else :
        fn = frobenius_number(a) 
        return fn + 1 if not fn == -1 else fn
