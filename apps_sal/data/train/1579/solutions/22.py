for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 a.sort(reverse=True)
 to_add=a[0]
 f=0
 for i in range(1,n):
  to_add=to_add|a[i]
  if to_add in a:
   f=1
   break
  a.append(to_add)
 if f==0:
  print("YES")
 else:
  print("NO")
