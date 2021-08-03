# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
 
 class Solution:
     def swapPairs(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
 
         if head is None or head.next is None:
             return head
         else:
             first = head
             second = first.next
             third = second.next
 
             second.next = first
             first.next = self.swapPairs(third)
             return second
