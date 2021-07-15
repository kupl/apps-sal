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
         i = 1
         node = head
         prev = None
         prev2 = None
         while node is not None:
             if i % 2 == 0 and i != 1:
                 if prev2 is not None:
                     prev2.next = node
                 prev.next = node.next
                 node.next = prev
                 if i == 2:
                     head = node
                 node = prev
             prev2 = prev
             prev = node
             node = node.next
             i += 1
         return head
