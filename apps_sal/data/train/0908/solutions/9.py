# cook your code here
test = int(input())
a=0
while(a<test):
  a = a+1
  n = int(input())
  sum = 0
  if n==1:
   print("1")
  else:    
   for i in range(1,n):
    sum = sum +i
    
    
    if(sum ==n):
     print(i)
     break
    elif(sum > n):
     print(i-1)
     break
    else:
     pass
