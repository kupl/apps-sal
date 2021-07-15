t=int(input())
for _ in range(0,t):
 intercept1=[]
 intercept2=[]
 n=int(input())
 for i in range(0,n):
  x,y=map(int,input().split())
  intercept1.append(y+x)
  intercept2.append(y-x)
 intercept1.sort()
 intercept2.sort()
 mn1=10**10
 mn2=10**10
 for i in range(1,n):
  diff1=intercept1[i]-intercept1[i-1]
  mn1=min(mn1,diff1)
  diff2=intercept2[i]-intercept2[i-1]
  mn2=min(mn2,diff2)
  ans=min(mn1,mn2)
 print(ans/2)
