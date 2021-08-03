# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def deleteDuplicates(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
         if head is None or head.next is None:
             return head
         dmy = ListNode (head.val - 1)
         dmy.next = head
         prev = dmy
         curr = dmy
         dul = dmy.val
         while curr:
             if curr.val == dul:
                 curr = curr.next
                 if curr:
                     continue
                 else:
                     prev.next = None
             else:
                 dul = curr.val
                 prev.next = curr
                 curr = curr.next
                 if curr and curr.val != dul:
                     prev = prev.next
         return dmy.next	
