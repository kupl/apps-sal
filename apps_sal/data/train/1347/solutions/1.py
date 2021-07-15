N,M=list(map(int,input().split()))
array=list(map(int,input().split()))
full=[[0]*3]*M
final=[[0]*3]*M
init=[[0]*3]*M
for i in range(M):
 full[i]=input().split()
 full[i][1]=int(full[i][1])
 full[i][0]=int(full[i][0])
k=0
y=0

for j in range(M):
 if (full[j][0] in array):
  final[k]=full[j]
  k+=1
 else:
  init[y]=full[j]
  y+=1

final=sorted(final,key=lambda x: x[1])
init=sorted(init,key=lambda x: x[1])
for i in range(k):
 print(final[M-1-i][2])
for i in range(y):
 print(init[M-1-i][2])

