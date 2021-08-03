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
         t = None
         c = None
         while head:
             if c is None or c != head.val:
                 t, head.next, head = head, t, head.next
                 c = t.val
             else:
                 while t and t.val == c:
                     t = t.next
                 head = head.next
         res = None
         while t:
             res, t.next, t = t, res, t.next
         return res
