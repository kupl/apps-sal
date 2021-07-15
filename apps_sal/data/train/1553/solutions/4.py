rows,columns=list(map(int,input().split()))
a=[[0] for i in range(rows+1)]
a[0]=[0 for i in range(columns+1)]
for i in range(1,rows+1):
 x=[int(i) for i in input().split()]
 s=0
 for j in range(columns):
  s+=x[j]
  a[i].append(s+a[i-1][j+1])
for i in range(int(input())):
 x1,y1,x2,y2=list(map(int,input().split()))
 s=a[x2][y2]-a[x2][y1-1]-a[x1-1][y2]+a[x1-1][y1-1]
 print(s)

