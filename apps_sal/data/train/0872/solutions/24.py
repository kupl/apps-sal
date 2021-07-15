# cook your dish here
t = int(input())
while(t>0):
 n,a,b,k = map(int,input().split())
 prob = 0
 for i in range(1,n+1):
  if(i%a and i%b):
   continue
  elif(i%a or i%b):
   prob += 1
 if(prob >= k):
  print("Win")
 else:
  print("Lose")
 t -= 1
