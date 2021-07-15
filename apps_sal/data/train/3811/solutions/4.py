import re
def largest_sum(s):
    s = s.split('0')
    m = 0
    for l in s:
      temp_s = sum(map(int, l))
      if temp_s > m :
        m = temp_s
    return m

