def paperwork(n, m):
  #Declaring the variable with a value makes it local instead of global
  ans = 0
  
  #Checks that n and m are > 0 before doing the math
  if n and m > 0:
    ans = n * m
  
  #Throws out any answers that are negative
  if ans <= 0:
    ans = 0
    
  #Returns the ans variable  
  return ans
