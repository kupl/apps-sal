# cook your dish here
for _ in range(int(input())):
 n = int(input())
 c = 0
 for i in range(n):
  S,J = map(int,input().split())
  if (J-S)>5:
   c+=1
 print(c)
