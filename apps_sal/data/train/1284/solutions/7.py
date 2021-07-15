for _ in range(int(input())):
 n = int(input())
 k = n//4
 # a,b,c = map(int,input().split())
 a = sorted(map(int,input().split()))
 a60 = (a[k-1],a[k])
 a75 = (a[2*k-1],a[2*k])
 a90 = (a[3*k-1],a[3*k])
 if a60[0]==a60[1] or a75[0]==a75[1] or a90[0]==a90[1] :
  print(-1)
 else :
  print(a60[1],a75[1],a90[1])

