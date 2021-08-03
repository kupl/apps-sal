# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 import math
 class Solution:
     def splitListToParts(self, root, k):
         """
         :type root: ListNode
         :type k: int
         :rtype: List[ListNode]
         """
         def length(node):
             result = 0
             while node is not None:
                 result += 1
                 node = node.next
             return result
         
         total = length(root)
         result = []
         current = root
         
         while k > 0:
             l = math.ceil(total / k)
             total -= l
             k -= 1
             
             if l == 0:
                 result.append(None)
                 continue
                 
             root = current
             for _ in range(l-1):
                 current = current.next
             result.append(root)
             current.next, current = None, current.next
             
         return result
