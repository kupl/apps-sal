def how_much_water(L,X,N):
 if N>2*X:
     return "Too much clothes"
 elif N<X:
     return "Not enough clothes"
 
 for i in range(X+1,N+1):
     L=(11*L)/10
 return round(L,2)
