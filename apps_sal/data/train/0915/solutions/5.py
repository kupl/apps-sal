# cook your dish here
t=int(input())
for _ in range(t):
 n= int(input())
 s=set(map(int,input().split()))
 if(n==len(s)):
  print(n)
 else:
  print(len(s))
