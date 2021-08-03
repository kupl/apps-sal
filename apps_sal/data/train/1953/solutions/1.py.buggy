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
         left = head
         right = head
         for _ in range(n):
             right = right.next
         if not right:
             return head.next
         
         while right.next:
             left = left.next
             right = right.next
         
         left.next = left.next.next
         return head
             
