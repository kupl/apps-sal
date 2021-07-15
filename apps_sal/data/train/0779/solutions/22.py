# cook your dish here
for i in range(int(input())):
 n = int(input())
 a = list(map(int,input().split()))
 a.sort()
 s= a[n-1]
 for i in range(n-1,0,-1):
  s= (s+a[i-1])/2 
 print(s)
