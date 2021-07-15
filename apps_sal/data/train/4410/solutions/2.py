from math import log10, floor, log

def count_sixes(n):
  k = floor(log10(3) + (n - 1)*log10(2))
  return k - (k*log(10) > (n - (n & 1))*log(2))

# x[n] = 2/3 + d if n is odd
# x[n] = 2/3 - d otherwise
# d = 1/(3*2**(n-1))
# k = log10(1/d)
# adjust k depending on carry/borrow from adding/subtracting d
# if n is odd:
#   k-1 if 1/(3*10**k) <= d
#   k   otherwise
# else:
#   k-1 if 2/(3*10**k) <= d
#   k   otherwise

