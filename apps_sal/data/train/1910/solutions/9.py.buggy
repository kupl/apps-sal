# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def reverseK(self, beg, end):        
         prev = None
         curr = beg
         while curr is not end:
             next_node = curr.next
             curr.next = prev
             prev = curr
             
             curr = next_node
             
         return prev, beg
             
         
     def reverseKGroup(self, head, k):
         """
         :type head: ListNode
         :type k: int
         :rtype: ListNode
         """
         if head is None:
             return None
         
         fake = ListNode(0)
         prev = fake
         curr = head
         
         while curr:
             i = 1
             tail = curr
             while i <= k and tail:
                 tail = tail.next
                 i += 1
             
             if i -1 == k:
                 new_curr = tail
                 r_head, r_tail = self.reverseK(curr, tail)
             else:
                 r_head = curr
                 r_tail = None
                 new_curr = None
             
             curr = new_curr
             prev.next = r_head
             
             if r_tail:
                 r_tail.next = curr
                 
             prev = r_tail
             
         return fake.next        
