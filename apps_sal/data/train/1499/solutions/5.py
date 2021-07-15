# cook your dish here
t=int(input())
while(t):
 n,m=map(int, input().split())
 a=[]
 for i in range(n):
  a.append(list(map(int, input().split())))
 # print(a)
 s=input()
 p,q=map(int, input().split())
 a0=[]
 a1=[]
 for i in range(n+m-1):
  a0.append(0)
  a1.append(0)
 for i in range(n):
  for j in range(m):
   if(a[i][j]==0):
    a0[i+j]+=1
   else:
    a1[i+j]+=1
 cost=0
 for i in range(len(s)):
  if(s[i]=='0'):
   cost+= min(p*a1[i] , (p*a0[i]+q))
  else:
   cost+= min(p*a0[i] , (p*a1[i]+q))
 print(cost)
 t-=1
