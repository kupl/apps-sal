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
         dummy = ListNode(0)
         new_head = dummy
         prev = None
         n = 0
         while head:
             if prev is None:
                 prev = head
                 n = 1
             elif head.val != prev.val:
                 if n < 2:
                     new_head.next = prev
                     new_head = prev
                 prev = head
                 n = 1
             else:
                 n += 1
 
             head = head.next
         if n == 1:
             new_head.next = prev
             new_head = new_head.next
         new_head.next = None
         return dummy.next
         
