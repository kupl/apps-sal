# cook your dish here
t=int(input())
for i in range(t):
 n=int(input())
 li=list(map(int,input().split(" ")))
 s=list(set(li))
 print(len(s)) 
  

