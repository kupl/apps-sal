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
         # Calculate length of linked list
         retList = []
         if root == None:
             for i in range(k):
                 retList.append([])
             return retList
         
         curr = root
         total_len = 1
         while(curr.next != None):
             curr = curr.next
             total_len += 1
         part_len = total_len // k
         r = total_len % k
         head = root
         prev = None
         for i in range(k):
            
             retList.append(head)
             if r>0:
                 inc = 1
             else:
                 inc = 0
             r -= 1
             for j in range(part_len+inc):
                 prev = head
                 head = head.next
             if prev:
                 prev.next = None
             
         return retList
