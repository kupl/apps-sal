for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 if(sum(l)>=0):
  print("YES")
 else:
  print("NO")
