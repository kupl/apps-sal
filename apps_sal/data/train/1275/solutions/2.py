for i in range(int(input())):
 n,m = (int(i) for i in input().split())
 li = [int(i) for i in input().split()]
 ma,mi = max(li),min(li)
 for i in range(n):
  print(max(ma-i,i-mi),end=' ')
 print()
