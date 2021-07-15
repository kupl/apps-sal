ans = [[False for _ in range(1001)] for _ in range(1001)]
for _ in range(int(input())):
 r,c = map(int,input().split())
 count = 0
 for i in range(0,r*c):
  val = 0
  for x in range(0,r*c,i+1):
   a = x//r
   b = x%r
   
   # ans.add((a,b))
   ans[a][b] = True
   a = x%c
   b = x//c
   # ans.add((a,b))
   ans[a][b]=True
   
  for x in range(0,r*c,i+1):
   
   a = x//r
   b = x%r
   
   if ans[a][b] == True:
    ans[a][b]=False
    val+=1
   a = x%c
   b = x//c
   if ans[a][b] == True:
    ans[a][b]=False
    val+=1
   
  
  print(val, end= " ")
