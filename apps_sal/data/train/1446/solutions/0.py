# from math import log2
# N = 10000
# for i in range(1,N):
#     # print(i)
#     for m in range(i):
#         if( (m^(m+1))==i ):
#             print(i)
#             print(m,m+1,bin(m)[2:])
#             print()
#             break
#     # else:
#         # print(-1)
#         # print()
T = int(input())
ans = []

for _ in range(T):
 N = int(input())

 # x = log2(N+1)
 if(N==1):
  ans.append(2)
 elif('0' not in bin(N)[2:]):
  ans.append(N//2)
 else:
  ans.append(-1)

for i in ans:
 print(i)
