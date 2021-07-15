# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def swapPairs(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
 
         dummy = ListNode(None)
         prev = dummy
         dummy.next = head
 
         left = head
         while left:
           if left.next is None:
             break
           right = left.next
           prev.next = right
           left.next, right.next = right.next, left
           prev = left
           left = left.next
 
         return dummy.next
