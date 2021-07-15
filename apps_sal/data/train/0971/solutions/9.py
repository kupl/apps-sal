# cook your dish here
for t in range(int(input())):
 n=int(input())
 a=[int(x)for x in input().rstrip().split()]
 b=list(set(a))
 max1=0
 for i in range(0,len(b)):
  s=a.count(b[i])
  if s>max1:
   max1=s
 print(n-max1)
