import bisect
import sys
sys.setrecursionlimit(10**7)

def dfs(v):
 #DFSの行き(子ノードに下っていくとき)の処理
 pos=bisect.bisect_left(dp,arr[v]) #最長増加部分列で更新する場所を2分探索により求める
 changes.append((pos,dp[pos])) #更新した要素とその値を記録しておく
 dp[pos]=arr[v]
 ans[v]=bisect.bisect_left(dp,10**18) #1からvまでの最長増加部分列の長さは、最長増加部分列の10**18以外の値の個数に等しい
 for u in g[v]:
   if checked[u]==0:
     checked[u]=1
     dfs(u)
 #DFSの戻り(親ノードに上っていくとき)の処理
 pos,val=changes.pop() #頂点vで更新した最長増加部分列の値を元に戻す
 dp[pos]=val

n=int(input())
arr=[0]+list(map(int,input().split()))
g=[[] for _ in range(n+1)]
for _ in range(n-1):
 a,b=map(int,input().split())
 g[a].append(b)
 g[b].append(a)
ans=[0]*(n+1)
checked=[0]*(n+1)
checked[1]=1
dp=[10**18 for _ in range(n+1)] #最長増加部分列を求めるのに、十分大きな値で初期化しておく
changes=[]
dfs(1)
for i in range(1,n+1):
 print(ans[i])
