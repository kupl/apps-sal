for _ in range(int(input())):
 n=int(input())
 c=0
 for i in range(1,n+1,2):
  k=n-i+1
  c+=k**2
 print(c)
