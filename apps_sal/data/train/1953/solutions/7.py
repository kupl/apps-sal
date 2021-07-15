# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     
     # one pass O(N) deletion approach using 2 ptr
     def removeNthFromEnd(self, head, n):
         """
         :type head: ListNode
         :type n: int
         :rtype: ListNode
         """
 
         # will point at node to be deleted
         slow = head
 
         # assists in finding the nth node from end
         fast = head
 
         # node before node to be deleted
         prev = None
 
         for i in range(n):
 
             fast = fast.next
 
         # want to delete head
         if fast == None:
 
             slow = head
             head = head.next
             slow.next = None
 
         # want to delete a node besides head
         else:
 
             while fast:
 
                 prev = slow
                 slow = slow.next
                 fast = fast.next
 
             prev.next = slow.next
             slow.next = None
 
         return head

