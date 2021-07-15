def finance(n):
    return sum( i*(2*i+1)-i*(i-1)/2  for i in range(1, n+1) )
