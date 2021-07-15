import numpy as np
t = int(input())
ans = []
for i in range(t):
 n,v1,v2 = [int(x) for x in input().split()]
 tc=(np.sqrt(2)*n*1000)/v1;
 te=(2*n*1000)/v2;
 if tc>te:
  ans.append("Elevator")
 elif tc<te:
  ans.append("Stairs")
for i in range(t):
 print(ans[i])
