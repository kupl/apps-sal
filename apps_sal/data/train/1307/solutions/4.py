# cook your dish here
s=pow(10,9)+7
a=[[0 for i in range(11)]for j in range(1001)]
for i in range(1,11):
 a[2][i]=i
for n in range(3,1001):
 for k in range(1,11):
  a[n][k]=pow(k,n-1,s)-a[n-1][k]
  if(a[n][k]<0):
   a[n][k]+=s
t=int(input())
for i in range(t):
 inp = list(map(int,input().split()))
 n=inp[0]
 k=inp[1]
 print(a[n][k])
