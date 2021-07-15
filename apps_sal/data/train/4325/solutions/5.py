def knight_rescue(N,x,y):
  return any(i%2==0 for i in N) or (x+y)%2==0
