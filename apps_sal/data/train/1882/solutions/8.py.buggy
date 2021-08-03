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
         previous = dummy
         previous.next = head
         node = head
         while node and node.next:
             end = node.next.next
             previous.next = node.next
             node.next.next = node
             node.next = end
             previous = previous.next.next
             node = previous.next
         return dummy.next
