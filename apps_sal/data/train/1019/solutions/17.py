# cook your dish here
for _ in range(int(input())):
 n = int(input())
 l = list(map(int,input().split()))
 f = True
 for i in range((n+1)//2):
  if l[i] != i+1:
   f = False
  if l[n-i-1] != i+1:
   f = False
 if n%2 == 0:
  f = False
 if f == True:
  print("yes")
 else:
  print("no")

