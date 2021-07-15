# cook your dish here
t=int(input())
x=[1,2,3,4,5,6,7]
for i in range(t):
 N=int(input())
 a=list(map(int,input().split())) 
 rev=a[::-1] 
 dup=set(a) 
 if rev== a and list(dup) ==x:    
  print("yes")
 else:
  print("no")
