t = int(input())
for i in range(t):
 x,y,k = map(int,input().split())
 s1 = x+y 
 s2 = s1//k 
 if(s2%2==0):
  print("Chef")
 else:
  print("Paja")
