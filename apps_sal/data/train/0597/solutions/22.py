for _ in range(int(input())):
 n = int(input())
 x_arr = []
 h_arr = []
 d = []
 D = []
 for i in range(n):
  x,y = map(int,input().split())
  x_arr.append(x)
  h_arr.append(y)
 for x in range(1,n):
  d.append(x_arr[x]-x_arr[x-1])
 D.append(d[0])
 for i in range(len(d)-1):
  D.append(d[i]+d[i+1])
 D.append(d[-1])
 h_arr.sort()
 D.sort()
 ans = 0
 for x in range(n):
  ans+=(D[x]*h_arr[x])
 print(ans)
