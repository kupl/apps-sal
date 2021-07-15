# cook your dish here
for _ in range(int(input())):
 n = int(input())
 l = list(map(int,input().split()))
 count = 1
 for i in range(1,5):
  k = [] + l[:i]
  if min(k)>l[i]:
   count+=1
 for i in range(5, n):
  k = [] + l[i-5:i]
  if min(k)>l[i]:
   count+=1
 print(count)
