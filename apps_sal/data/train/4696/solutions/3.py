def same_encryption(s1, s2):
  def single_digit(s):
      total = len(s) - 2
      while total > 9:
          total = sum(int(d) for d in str(total))
          
      return "{}{}{}".format(s[0], total, s[-1])
      
  return single_digit(s1) == single_digit(s2)
