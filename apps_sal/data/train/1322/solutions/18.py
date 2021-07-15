# cook your dish here
for t in range(int(input())):
 n,k=map(int,input().split())
 a=[int(i) for i in input().split()]
 a.sort()
 a=a[::-1]
 count=k
 while k<n and a[k-1]==a[k]:
  count+=1
  k+=1
 print(count)
