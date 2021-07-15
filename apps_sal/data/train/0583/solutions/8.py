# cook your dish here
for i in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 if(sum(a)>=0):
  print("YES")
 else:
  print("NO")
