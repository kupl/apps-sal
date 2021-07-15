def digits(n):
  len_1=0
  while(n!=0):
    n//=10
    len_1+=1
  return len_1

