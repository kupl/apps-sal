for _ in range(int(input())):
 n = int(input())
 lis = list(map(int,input().split()))
 maxx = []
 for i in range(n):
  maxx.append(lis[i]+i)
 print(max(maxx))
