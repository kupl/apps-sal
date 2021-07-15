t=int(input())
for i in range(t):
 s=list(map(int,input().split()))
 s.sort()
 if s[2]>s[0]+s[1]+1:
  print("No")
 else:
  print("Yes")

