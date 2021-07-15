# Helpful math trivias: 
# ---------------------
# 1. if "x" is in the sequence of the 'a's, then 
#    5*13*y+x is also in the sequence of 'a's
# 2. the base solutions are 4, 9, 56, 61
# 3. if the sequence is terminated at the right point,
#    then it is the mix of 4 independent arithmetic
#    sequences (x=130*n**2 is the total sum of the four)

import math

def find_closest_value(x):
   if x < 4:
      return 4

   n = math.sqrt(x/130)
   n_low = math.floor(n)
   seed = 130*n_low**2
   n_inc = n_low*65
   candidates = [seed,
                 seed+4  +1*n_inc,
                 seed+13 +2*n_inc,
                 seed+69 +3*n_inc,
                 seed+130+4*n_inc]
   candidates=sorted(candidates,reverse=True)
   candidates=sorted(candidates,key=lambda a:abs(a-x))
   return candidates[0]
