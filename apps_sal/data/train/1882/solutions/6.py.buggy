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
         
         def swapTwo(head):
             if not head.next:
                 return head
             elif not head.next.next:
                 tmp = head.next
                 head.next = None
                 tmp.next = head
                 return tmp
             else:
                 tmp = head.next
                 head.next = swapTwo(tmp.next)
                 tmp.next = head
                 return tmp
         
         if not head:
             return head
         else:
             return swapTwo(head)
