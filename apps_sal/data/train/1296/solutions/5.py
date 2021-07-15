import queue, fractions
class Node:
 def __init__(self, i):
  self.val = i
  self.children = []
mod = 10**9+7
for t in range(int(input())):
 n = int(input())
 d = []
 for i in range(n+1):
  d.append(Node(i))
 edges = []
 for i in range(n-1):
  a, b = list(map(int, input().split()))
  d[a].children.append(b)
  d[b].children.append(a)
 root = int(input())
 l = len(d[root].children)
 ans = 1
 while (l>0):
  ans*=l
  ans%=mod
  l-=1
 
 for i in d[root].children :
  count = 0
  # get leaf nodes
  q = queue.Queue()
  q.put((i, root))
  while (not q.empty()):
   #print "size ",q.qsize()
   n, p = q.get()
   #print n,p, "- pop"
   flag = 1
   for c in (d[n].children):
    if (c!=p):
     q.put((c,n))
     flag = 0
   if (flag == 1):
    count+=1
  #print count
  ans *= count
  ans %= mod
 print(ans)
 #print "*****"

