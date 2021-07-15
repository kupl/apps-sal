# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 
         #"""
         #:type head: ListNode
         #:rtype: ListNode
         #"""
 
 class Solution:  
     # @param head, a ListNode  
     # @return a ListNode  
     def deleteDuplicates(self, head):
         pre = ListNode(0)
         dummy = pre
         dummy.next = head
         while head and head.next:
             if head.val == head.next.val:
                 while head and head.next and head.val == head.next.val:
                     head = head.next
                 head = head.next
                 pre.next = head
             else:
                 pre = pre.next
                 head = head.next
         return dummy.next
