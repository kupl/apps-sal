# cook your dish here
for _ in range(int(input())):
 n = int(input())
 a = list(map(int,input().split()))
 sum = []
 temp = 0
 for i in range(n):
  temp += a[i]%2
  sum.append(temp)
 q = int(input())
 # print(sum)
 while q!=0:
  q -= 1 
  l,r = [int(x) for x in input().split()]
  l -= 1 
  r -= 1 
  if sum[r]-sum[l]+a[l]%2==r-l+1:
   print("ODD")
  else:
   print("EVEN")

