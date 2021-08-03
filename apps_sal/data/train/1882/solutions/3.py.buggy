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
         node = head
         while node and node.next :
             node.val, node.next.val = node.next.val, node.val
             node = node.next.next
         return head
                 
