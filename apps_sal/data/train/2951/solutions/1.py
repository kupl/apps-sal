def how_many_measurements(n):
  if n>1: 
      return 1 + how_many_measurements(n/3) 
  return 0
