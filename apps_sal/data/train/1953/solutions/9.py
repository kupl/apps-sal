# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def removeNthFromEnd(self, head, n):
         """
         :type head: ListNode
         :type n: int
         :rtype: ListNode
         """
         current = head
         while current is not None:
             i = n
             runner = current.next
             while i > 1:
                 if runner is not None:
                     runner = runner.next
                     i -= 1
             if runner is None:
                 return head.next
             elif runner.next is None:
                 current.next = current.next.next
                 return head
             
             current = current.next
         return head
