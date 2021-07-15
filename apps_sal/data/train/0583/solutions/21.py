# cook your dish here
t = int(input())
for x in range(t):
 n=int(input())
 l = [int(i) for i in input().split()]
 s = sum(l)
 if(s>=0):
  print("YES")
 else:
  print("NO")
