# cook your dish here
for _ in range(int(input())):
 n=int(input())
 x=int(input())
 a=list(map(int,input().split()))
 day=1
 ans="Possible"
 a.sort()
 for i in range(0,len(a),x):
  if a[i]<=day:
   ans="Impossible"
   break
  else:
   day+=1
 print(ans)
