a = [[0]*1010 for x in range(1010)]
for i in range (1007):
 a[0][i]=0
for i in range (1007):
 a[i][0]=1
for i in range(1,1005):
 for j in range(1,i+1):
  a[i][j]=a[i-1][j-1]+a[i-1][j]
 
test = int(input())
while test>0:
 sum=0.0
 s, n, m, k=list(map(int, input().split()))
 if(s==1):
  print(1.000000)
  test=test-1
  continue
 r=a[s][n]
 for i in range(k,m):
  p=a[m][i+1]
  if((n<i+1) or (s-m)<(n-(i+1))):
   q=0
  else:
   q=a[s-m][n-(i+1)]
  sum=sum+(float(p*q*(i+1)*s))
 sum=sum/(float(r*m*n))
 print("%.6f" % sum)
 test=test-1
