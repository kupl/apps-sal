def is_even(n):
  if type(n) == int:
    if (n % 2) == 0:  
      t_f = True  
    else:  
      t_f = False
  else:
    t_f = False
  return(t_f)  

