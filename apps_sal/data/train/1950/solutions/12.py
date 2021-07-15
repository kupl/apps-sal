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
         
         res = ListNode(0)
         p = res        
         cnt = 0
         while head:
             if cnt == 0:
                 candidate = head.val
                 cnt += 1
             elif candidate != head.val:
                 if cnt == 1:
                     p.next = ListNode(candidate)
                     p = p.next
                 candidate = head.val
                 cnt = 1
             else: 
                 cnt += 1
             head = head.next
         
         if cnt == 1:
             p.next = ListNode(candidate)
         return res.next
                 
             
