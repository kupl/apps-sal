# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def splitListToParts(self, root, k):
         """
         :type root: ListNode
         :type k: int
         :rtype: List[ListNode]
         """
         res=[]
         ans=[]
         for i in range(k):
             res.append([])
         while root:
             ans.append(root.val)
             root=root.next
             
         l=len(ans)
         l1=l//k
         l2=l%k
         print(l1,l2)
         for i in range(k):
             if l2>0:
                 for j in range(l1+1):
                     res[i].append(ans.pop(0))
             else:
                 for j in range(l1):
                     res[i].append(ans.pop(0))
             print(res)
             l2-=1
         return res
             
