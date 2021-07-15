import sys
import bisect
#input=sys.stdin.readline
#t=int(input())
t=1
for _ in range(t):
 n,m=map(int,input().split())
 #n=int(input())
 l=[]
 #l=list(map(int,input().split()))
 arr=[[0 for j in range(m+2)] for i in range(n+2)]
 for i in range(n):
  l.append(input())
 #print(arr)        
 q=int(input())
 for __ in range(q):
  x1,y1,x2,y2=map(int,input().split())
  arr[x1][y1]+=1;
  arr[x2+1][y1]-=1
  arr[x1][y2+1]-=1
  arr[x2+1][y2+1]+=1
 for i in range(1,n+1):
  for j in range(1,m+1):
   x1=(arr[i-1][j]+arr[i][j-1])
   y1=(x1-arr[i-1][j-1])
   arr[i][j]=(arr[i][j]+y1)
   
   #arr[i][j]%=2
   print((arr[i][j]+int(l[i-1][j-1]))%2,end="")
  print() 
 print() 
  
