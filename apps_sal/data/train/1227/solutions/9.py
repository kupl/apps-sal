pairwise=[[0,2,4],[0,3,4],[1,3,4],[1,2,4],
   [0,2,5],[0,3,5],[1,3,5],[1,2,5]]
for _ in range(int(input())):
 c=input().split()
 ans="NO"
 for i in pairwise:
  x,y,z=i
  if c[x]==c[y]==c[z]:
   ans="YES"
   break
 print(ans)
