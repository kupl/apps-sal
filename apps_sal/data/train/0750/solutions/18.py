while True:
 n=int(input())
 if n==0:
  break
 li=list(map(int, input().split()))
 
 x=[0]*n


 for i in range(n):
  z=li[i]
  x[z-1]=i+1

 if x==li:
  print("ambiguous")
 else:
  print("not ambiguous")
