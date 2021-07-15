coeff=[[1],[0.5,0.5]]
for i in range(2,1001):
 l1=[]
 l1.append(1-(coeff[-1][0])/2)
 for j in range(1,i):
  p=(coeff[-1][j]+coeff[-1][j-1])/2 
  l1.append(1-p)
 l1.append(l1[0])
 coeff.append(l1)
for i in range(int(input())):
 n=int(input())

 arr=[int(i) for i in input().split()]
 ans=0
 for i in range(n):
  ans+=arr[i]*coeff[n-1][i]
 print(ans)
