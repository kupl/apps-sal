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
         # get the length of list:
         node = root
         total = 0
         while node:
           total += 1
           node = node.next
 
         avg = int(total / k)
         extras = total % k
         result = [None] * k
         
         curr = root
         for i in range(k):
           result[i] = curr
           if extras > 0:
             steps = avg + 1
             extras -= 1
           else:
             steps = avg
           prev = None
           for j in range(steps):
             prev = curr
             curr = curr.next
           
           if prev:
             prev.next = None
         
         return result
 
             
             
         
         
         
