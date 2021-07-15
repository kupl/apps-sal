# cook your dish here
t=int(input())
for i in range(t):
 n,k=[int(i) for i in input().split()]
 s=input()
 u=0
 l=0
 for i in range(len(s)):
  if(s[i].isupper()):
   u+=1 
  else:
   l+=1
 if(u<=k and l<=k):
  print("both")
 elif(l<=k and u>k):
  print("brother")
 elif(u<=k and l>k):
  print("chef")
 else:
  print("none")

