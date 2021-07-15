from bisect import bisect
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 c=[]
 for _ in range(int(input())):
  x,y=map(int,input().split())
  s=x+y
  st=0
  end=n-1
  t=True
  while(st<=end):
   half=(end+st)//2
   if (l[half]==s):
    t=False
    break
   elif(l[half]>s):
    end=half-1
   else:
    st=half+1
  print(bisect(l,s) if t else -1)
