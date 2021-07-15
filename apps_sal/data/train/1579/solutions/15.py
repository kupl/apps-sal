# cook your dish here
def subArrayBitWiseOR(A):
 res=set()
 pre={0}
 for x in A:
  pre={x | y for y in pre} | {x}
  res|=pre
 return(len(res))
t=int(input())
while(t>0):
 t-=1
 n=int(input())
 a=list(map(int,input().split()))
 d=subArrayBitWiseOR(a)
 if(d==(n*(n+1))/2):
  print("YES")
 else:
  print("NO")
