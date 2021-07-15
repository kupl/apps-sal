# cook your dish here
T=int(input())
for i in range(T):
  N=int(input())
  sum1=0
  a=list(map(int,input().split()))
  for i in a:
    j=i&1
    if(j==0):
      sum1+=i
  print(sum1)
