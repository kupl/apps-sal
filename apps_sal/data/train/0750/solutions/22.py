# cook your dish here
t=int(input())
while(t):
 l=list(map(int,input().split()))
 k=10
 for i in range(len(l)):
  if(l[l[i]-1]!=i+1):
   print("not ambiguous")
   k=1
   break
 if(k==10):
  print("ambiguous")
 t=int(input())
