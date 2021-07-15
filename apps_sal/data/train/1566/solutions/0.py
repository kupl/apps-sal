import sys
sys.setrecursionlimit(1000000)

mod = 10**9 + 7
ts = int(input())
while ts > 0:
 n,q = list(map(int,input().split()))
 ncc = n-1
 par = [i for i in range(n)]
 rank = [1]*n
 xor = [0]*n
 flag = 1

 def find(a):
  if par[a] == a:
   return a
  else:
   temp = find(par[a])
   xor[a]^=xor[par[a]]
   par[a] = temp
   return temp

 def union(a,b): 
  a,b = find(a),find(b)
  if a ==b:
   return 
  if rank[a] > rank[b]:
   par[b] = a

   rank[a]+=rank[b]
  elif rank[a] < rank[b]:
   par[a] = b
   rank[b]+=rank[a]
  else:
   par[b] = a
   rank[a]+=rank[b]
  par[b] =a

 for _ in range(q):
  
  a,b,x = list(map(int,input().split()))
  a-=1
  b-=1
  if flag == -1:
   continue
  para = find(a)
  parb = find(b)

  if para == parb and xor[a] ^ xor[b] != x:
   flag = -1 
   continue
   # print("no")

  if para != parb:
   if rank[para] < rank[parb]:
    xor[para] = xor[a] ^ xor[b] ^ x
    par[para] = parb
    rank[parb]+=rank[para]
   else:
    xor[parb] = xor[a] ^ xor[b] ^ x
    par[parb] = para
    rank[para]+=rank[parb]
   ncc-=1
   
 if flag != -1:
  print("yes")
 else:
  print("no")
  
 ts-=1
