# cook your dish here
for i in range(int(input())):
 n=int(input())
 l=[int(x) for x in input().split()]
 count=0
 sumv=0
 for i in range(n):
  count+=1
  if i!=n-1 and l[i]>l[i+1]:
   sumv+=int(((count+1)*count)/2)
   count=0
 sumv+=int(((count+1)*count)/2)
 print(sumv)
