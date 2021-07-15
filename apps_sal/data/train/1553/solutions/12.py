l = input().split()
n=int(l[0])
m=int(l[1])
l=[]
for _ in range(n):
 l.append(list(map(int,input().split()))[:])
tc = int(input())
for _ in range(tc):
 dim = input().split()
 r1 = int(dim[0])
 c1 = int(dim[1])
 r2 = int(dim[2])
 c2 = int(dim[3])
 sum=0
 for i in range(r1-1,r2):
  for j in range(c1-1,c2):
   sum+=l[i][j]
 print(sum)
 

