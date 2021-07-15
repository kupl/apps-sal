# cook your dish here
n=int(input())
for i in range(0,n):
 (a,b)=list(map(int,input().split()))
 if(a%2==0 or b%2==0):
  print("YES")
 else:
  print("NO")
