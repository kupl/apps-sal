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
         if not head or not head.next:
             return head
         fakehead = ListNode(0)
         fakehead.next = head
         prev = fakehead
         slow = head
         fast = head.next
         while fast:
             if fast.val == slow.val:
                 while fast and fast.val == slow.val:
                     fast = fast.next
                 slow = prev
             else:
                 prev = slow
                 slow = slow.next
                 slow.val = fast.val
                 fast = fast.next
         slow.next = None
         return fakehead.next
         
