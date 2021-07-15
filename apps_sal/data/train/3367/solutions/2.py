def routes(n):
  if(n < 1):
    return(0);
  
  res = 1;
  for i in range(1, n + 1):
    res = res*(n + i)//i;
    
  return(res);
