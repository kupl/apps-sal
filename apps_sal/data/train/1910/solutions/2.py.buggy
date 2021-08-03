# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def reverse(self, start, end):
         head = ListNode(0)
         head.next = start
         while head.next != end:
             temp = start.next
             start.next = temp.next
             temp.next = head.next
             head.next = temp
         return [end, start]
     
     def reverseKGroup(self, head, k):
         """
         :type head: ListNode
         :type k: int
         :rtype: ListNode
         """
         if head is None or head.next is None:
             return head
         dummpy = ListNode(0)
         dummpy.next = head
         phead = dummpy
         while phead.next:
             start, end = phead.next, phead.next
             for i in range(k-1):
                 end = end.next
                 if end is None:
                     return dummpy.next
             result = self.reverse(start, end)
             phead.next = result[0]
             phead = result[1]
         return dummpy.next
             
