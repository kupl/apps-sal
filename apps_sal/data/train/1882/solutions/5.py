# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     # Iteratively
     def swapPairs(self, head):
         r = p = ListNode(0)
         r.next = head
 
         '''
             h h.n h.n.n
         '''
         while head and head.next:
             t = head.next
 
             head.next = t.next
             t.next = head
 
             p.next = t
             
             p = t.next
             head = head.next
 
         return r.next
 
         
