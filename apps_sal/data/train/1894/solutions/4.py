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
         
         n = 0
         res = []
         def deepth(root):
             if root == None:
                 return 0
             if root.next == None:
                 return 1
             return 1 + deepth(root.next)
         n = deepth(root)
         if n <= k:
             for i in range(n):
                 res.append([root.val])
                 root = root.next
             for i in range(k-n):
                 res.append([])
         if n > k:
             j = [n//k]*k
             for i in range(n%k):
                 j[i] += 1
             for i in j:
                 temp = []
                 for k in range(i):
                     temp.append(root.val)
                     root = root.next
                 res.append(temp)
         return res
