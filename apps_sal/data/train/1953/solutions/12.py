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
         if head is None:
             return None
         fast = head
         slow = head
         for i in range(0, n):
             slow = slow.next
         if slow is None:
             return head.next
         while slow.next is not None:
             slow = slow.next
             fast = fast.next
         fast.next = fast.next.next
         
         return head
         
