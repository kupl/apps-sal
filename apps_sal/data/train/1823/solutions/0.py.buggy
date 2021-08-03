# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def reorderList(self, head):
         """
         :type head: ListNode
         :rtype: void Do not return anything, modify head in-place instead.
         """
         if not head:
             return 
         fast, slow = head.next, head
         while fast and fast.next:
             fast = fast.next.next
             slow = slow.next
             
         
         p = slow.next
         slow.next = None
         node = None
         while p:
             nxt = p.next
             p.next = node
             node = p
             p = nxt
         
         p = head
         while node:
             tmp = node.next
             node.next = p.next
             p.next = node
             p = p.next.next
             node = tmp
             
             
