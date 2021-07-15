t = int(input())
for _ in range(t):
 n,m,k = map(int,input().strip().split())
 plants = []
 stat = {}
 count = 0
 for i in range(k):
  x,y = map(int,input().strip().split())
  ele = (x,y)
  stat [ele] = 1
  plants.append([x,y])
  count += 4 
  if(stat.get((x-1,y)) == 1):
   count -= 2
  if(stat.get((x,y+1)) == 1):
   count -= 2
  if(stat.get((x+1,y)) == 1):
   count -= 2
  if(stat.get((x,y-1)) == 1):
   count -= 2
 print(count)
