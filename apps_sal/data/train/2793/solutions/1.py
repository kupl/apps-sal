from math import sqrt, ceil

# 1st group spends in the hotel s days,
#  2nd group - s + 1 days,
#  3rd group - s + 2 days,
#  ...,
#  nth group - s + n - 1 days.
#
# The total number of days for n groups: n * (s + s + n - 1) / 2 
#  (by the formula of arithmetic series).
# Let d be the last day of the nth group. Then
#  n * (s + s + n - 1) / 2 = d, 
#  n**2 + (2*s-1)*n - 2*d = 0,  
#  The only possible root of this quadratic equation equals
#  1/2 * (-p + sqrt(p**2 - 4*q), where p = 2*s - 1, q = 2*d.  
#  Thus, n = (1 - 2*s + sqrt((2*s - 1)**2 + 8*d)) / 2.
# But if d is not the last day of the group n, then n will be fractional,
#   and we have to round it up (get the ceiling of n).

def group_size(s, d):
    n = ceil((1 - 2*s + sqrt((2*s - 1)**2 + 8*d)) / 2)
    return s + n - 1
