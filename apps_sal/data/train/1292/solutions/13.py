def solve(grid,row,col,white):
 s=0
 for thing in grid[row]:
  for i in range(col,len(grid[row])):
   if grid[row][i]=='B':
    s=i-col+1
    return s
   elif grid[row][i]=='W':
    white+=1
   if white==2:
    s=i-col+1
    return s
   if i+1==len(grid[row]):
    s=i-col+1
    return s
 return s

arr = [int(x) for x in input().split()]
n,m,w,b = arr[0],arr[1],arr[2],arr[3]

arr = arr[4:]

wh = []
bl = []

g = [['.' for i in range(m)]for j in range(n)]

for i in range(0,2*w-1,2):
 g[arr[i]-1][arr[i+1]-1]='W'
for i in range(2*w,len(arr)-1,2):
 g[arr[i]-1][arr[i+1]-1]='B'

s=0
for i in range(n):
 c=0
 for j in range(m):
  if g[i][j]=='W' or g[i][j]=='B':
   c=0
   continue
  if c==0:
   c=solve(g,i,j,0)
   s+=c
  else:
   c-=1
   s+=c
print(s)

