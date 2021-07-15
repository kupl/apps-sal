# from collections import Counter
# class Node(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.rich = None
#         self.left = None
#         self.right = None

# class SegmentTree(object):
#     def __init__(self):
#         self.root = None
 
#     def addToTree(self, l, r, string):
#         node = Node(l,r)

#         if r == len(string) - 1:
#             self.root = Node(l,r)
#             node = self.root
  
#         if r - l < 3:
#             node.rich = False
#             return node
#         else:
#             m = int((l+r)/2)
#             left, right = self.addToTree(l, m, string), self.addToTree(m+1, r,     string)
#             node.weight = any()
#             node.left = left
#             node.right = right
#             return node
  
# T = int(input())        
# for _ in range(T):
#     N, Q = map(int,input().split())
#     string = input()
#     ans = 1
#     for __ in range(Q):
#         L, R = map(int, input().split())
#         if R-L >= 2:
#             L -= 1
#             sub_str = string[L:R]
#             cnt = Counter(sub_str)
#             for value in cnt.values():
#                 if value > 2:
#                     ans = 0
#                     print('yes')
#                     break
#         else:
#             ans = 0
#             print('no')

#         if ans:
#             print('no')

t=int(input())
for _ in range(t):
 n,q=map(int,input().split())
 s=input()
 dp=[0]*(n+1)
 for i in range(n-2):
  p=s[i:i+3]
  if p.count(p[0])>=2 or p.count(p[1])>=2:
   dp[i+1]=dp[i]+1
  else:
   dp[i+1]=dp[i]
 for _ in range(q):
  l,r=map(int,input().split())
  if n<3 or (r-l)<2:
   print("NO")
   continue
  if dp[r-2]-dp[l-1]>0:
   print("YES")
  else:
   print("NO")
