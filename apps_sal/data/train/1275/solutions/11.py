for _ in range(int(input())):
 n,m=map(int,input().split())
 l=list(map(int,input().strip().split(" ")))
 l.sort()
 for i in range(n):
  print(max(abs(i-l[-1]),abs(l[0]-i)),end=" ")
 print()
