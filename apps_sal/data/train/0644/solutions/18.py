for _ in range(int(input())):
 n=int(input())
 l1=list(map(int,input().split()))
 if(sum(l1)%n==0):
  print("Yes")
 else:
  print("No")
