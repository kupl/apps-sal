# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def deleteDuplicates(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
         if head == None:
             return None
         
         loop = head
         loop1 = head
         d = {}
         
         while loop:
             if loop.val in d.keys():
                 d[loop.val] += 1
             else:
                 d[loop.val] = 1
             loop = loop.next
         
         while loop1.next:
             if d[loop1.next.val] > 1:
                 loop1.next = loop1.next.next
             else:
                 loop1 = loop1.next
                 
         if d[head.val] > 1:
             return head.next
         else:
             return head
                 
         
