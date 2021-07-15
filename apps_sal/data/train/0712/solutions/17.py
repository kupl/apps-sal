# cook your dish here
t = int(input())
while t:
 t -= 1
 n = int(input())
 ls = list(map(int,input().split()))
 flag=1
 for item in ls:
  if item%2==0:
   flag=0
   break
 if flag==0:
  print("NO")
 else:
  print("YES")
