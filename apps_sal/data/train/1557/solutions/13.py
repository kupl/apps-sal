# cook your dish here
t=int(input())
for i in range(t):
 n=int(input())
 s1 = list(input())
 s2 = list(input())
 s1.sort()
 s2.sort()
 if s1==s2:
  print("YES")
 else:
  print("NO")

