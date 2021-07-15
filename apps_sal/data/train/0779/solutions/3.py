# cook your dish here
for t in range(int(input())):
 n=int(input())
 lis=list(map(int,input().split()))
 for i in range(n-1):
  lis.sort() 
  
  a=lis.pop(len(lis)-1)
  b=lis.pop(len(lis)-1) 
  
  lis.append((a+b)/2)
 print(lis[0]) 

