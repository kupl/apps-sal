for _ in range(int(input())):
 n = int(input())
 arr = []
 height = []
 d = []
 final = []
 for i in range(n):
  x,y = map(int,input().split())
  arr.append(x)
  height.append(y)
 for x in range(1,n):
  d.append(arr[x]-arr[x-1])
 final.append(d[0])
 for i in range(len(d)-1):
  final.append(d[i]+d[i+1])
 final.append(d[-1])
 height.sort()
 final.sort()
 ans = 0
 for x in range(n):
  ans+=(final[x]*height[x])
 print(ans)
