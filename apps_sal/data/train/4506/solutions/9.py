def geometric_sequence_elements(a, r, n):
  string = ""
  for x in range(0,n):
    if x!=n-1:
      string += str(a * (r ** x)) + ", "
    else:
      string += str(a * (r ** x))
  return(string)
