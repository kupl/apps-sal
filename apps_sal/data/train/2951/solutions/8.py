def how_many_measurements(n):
  if n>1:
      return 1 + how_many_measurements( n//3 + int(0.5 + (n%3)/2) ) 
  return 0
