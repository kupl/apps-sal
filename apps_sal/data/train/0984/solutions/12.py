for i in range(int(input())):
 n = int(input())
 l = list(map(int,input().split()))
 c = p = 0
 for i in range(n):
  if l[i]%2==0:
    c+=1
  else:
   p+=c
 print(p) 
