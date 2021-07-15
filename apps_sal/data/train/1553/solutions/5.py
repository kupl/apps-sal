rows,columns=list(map(int,input().split()))
a=[[0] for i in range(rows)]
for i in range(rows):
 x=[int(i) for i in input().split()]
 s=0
 for j in x:
  s+=j
  a[i].append(s)
for i in range(int(input())):
 x1,y1,x2,y2=list(map(int,input().split()))
 s=0
 for j in range(x1-1,x2):
  s+=a[j][y2]-a[j][y1-1]
 print(s)

