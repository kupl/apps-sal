def has_subpattern(s):
      l = len(s)
      for i in range(1,l//2+1):
         if not l%i and s[:i]*(l//i) == s : 
             return True
      return False  
