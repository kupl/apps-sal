# cook your dish here
n=int(input())
for i in range(n):
 num=int(input())
 d={}
 for j in range(num):
  s=input()
  a=int(input())
  d[a]=s
 
 for j in sorted (d):
  print(d[j])
