def modified_sum(a, n):
      s1=0
      s2=0
      for x in a:
          s1+=x**n
          s2+=x
      return s1-s2
