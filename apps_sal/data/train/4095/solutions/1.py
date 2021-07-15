def added_char(s1, s2):  
  for i in s2:
      if s1.count(i) != s2.count(i):
          return i
