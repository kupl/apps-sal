# cook your dish here
for T in range(int(input())):
 n,k = map(int,input().split())
 ls = list(map(int,input().split()))
 maxi = max(ls)
 if maxi>=k:
  print("YES")
 else:
  print("NO")
