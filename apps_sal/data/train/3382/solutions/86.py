def lowercase_count(strng):
  lowercase = ''.join(c for c in strng if c.islower())

  return(len(lowercase))
