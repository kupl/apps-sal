'''input
1
3
1 2
1 3
1 2 3
'''
import sys
sys.setrecursionlimit(1000000)
for _ in range(eval(input())):
 C=[]
 n=eval(input())
 for i in range(n):
  C.append([])
 for i in range(n-1):
  a,b=[int(x)-1 for x in input().split()]
  C[a].append(b)
  C[b].append(a)
 cnt=0
 Co=[bin(int(x)).count("1") for x in input().split()]
 Q=[0]*(n+100)
 cur=0
 done=[0]*n
 done[0]=1
 H=[0]*n
 for i in range(n):
  r=Q[i]
  if H[r]&1 == Co[r]&1:
   cnt+=1
  for i in C[r]:
   if done[i]==0:
    done[i]=1
    Q[cur+1]=i
    cur+=1
    H[i]=H[r]+1
 #dfs(0,-1)
 print(cnt*(n-cnt))


