# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def reverse(self, head, k):
         """
         :type head: ListNode
         :type k: int
         :rtype: ListNode
         """
         counter = k
         tail = head
         prev = None
         current = head
         
         while counter > 0 and current:
             newCurrent = current.next
             current.next = prev
             prev = current
             current = newCurrent
             counter -= 1
         
         if counter > 0:
             return self.reverse(prev, k - counter)
         
         head = prev
             
         return (head, tail, current)
     
     def reverseKGroup(self, head, k):
         """
         :type head: ListNode
         :type k: int
         :rtype: ListNode
         """
         if k == 0:
             return head
         
         head, tail, current = self.reverse(head, k)
         while current:
             joinedFragmentHead, newTail, newCurrent = self.reverse(current, k)
             tail.next = joinedFragmentHead
             tail = newTail
             current = newCurrent
             
         return head
