nCr = [[0 for x in range(1001)] for x in range(1001)]

for i in range (0,1001):
 nCr[i][0]=1
 nCr[i][i]=1
for i in range (1,1001):
 for j in range (1,1001):
  if i!=j:
   nCr[i][j] = nCr[i-1][j] + nCr[i-1][j-1]

#print(nCr[4][2])

t=eval(input())
for __ in range(0,t):
 s=input().split()
 s,n,m,k=int(s[0]),int(s[1]),int(s[2]),int(s[3])
 if (s==n):
  print("1.000000")
  continue
 
 foo=float(0.0000000)
 s=s-1
 n=n-1
 m=m-1
 bar=float(nCr[s][n])
 x=k-1
 if(k>n):
  print("0.000000")
  continue
 for i in range(0,x+1):
  foo=foo+(nCr[m][i]*nCr[s-m][n-i])
 
 ans= float(1- (foo/bar))
 print(ans)
 

