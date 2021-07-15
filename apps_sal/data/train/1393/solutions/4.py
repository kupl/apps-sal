# cook your dish here
for _ in range(int(input())):
 n=int(input())
 l=[int(item) for item in input().split(maxsplit=n)[:n]]
 count=1
 mini=l[0]
 if n==1:
  print(1)
 else:
  for i in range(1,n):
   if l[i]<=mini:
    mini=l[i]
    count=count+1
  print(count) 
