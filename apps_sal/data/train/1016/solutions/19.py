# cook your dish here
for _ in range(int(input())):
 n=int(input())
 count=0
 for i in range(n):
  x,y=list(map(int,input().split()))
  if y-x>5:
   count+=1
 print(count)

