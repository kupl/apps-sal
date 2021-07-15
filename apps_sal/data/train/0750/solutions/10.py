# cook your dish here
def invper(ar):
 ar1=[0]*(len(ar))
 for i in range(len(ar)):
  ar1[ar[i]-1]=i+1
 return ar1
t=int(input())
while(t!=0):
 ar=list(map(int,input().split()))
 ar1=invper(ar)
 if(ar==ar1):
  print("ambiguous")
 else:
  print("not ambiguous")
 t = int(input())
