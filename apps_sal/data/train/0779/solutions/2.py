# cook your dish here
t=int(input())
for i in range(t):
 n=int(input())
 N=list(map(int,input().split()))
 N.sort()
 
 k=n-1
 ave=N[k]
 for j in range(n-1):
  ave=(ave+N[k-1])/2
  k=k-1
  
 print(ave)
