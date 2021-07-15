def could_be(original, another):

  s1, s2 = set(another.split()), set(original.split())
  
  return len(s1) > 0 and len(s2) > 0 and s1 <= s2
