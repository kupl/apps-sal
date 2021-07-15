for t in range(int(input())):
 n=int(input())
 height=[]
 d=[]
 prev=0
 points=[]
 nex=0
 for i in range(n):
  x,h=[int(x) for x in input().split()]
  height.append(h)
  points.insert(i,x)
 for i in range(1,n):
  diff=points[i]-points[i-1]
  d.append(diff)
 points=[]
 for i in range(n-1):
  num=d[i]+prev
  prev=d[i]
  points.append(num)
 points.append(d[n-2])
 points.sort(reverse=True)
 height.sort(reverse=True)
 s=0
 for i in range(n):
  s+=(height[i]*points[i])
 print(s)
 
  
  
  

