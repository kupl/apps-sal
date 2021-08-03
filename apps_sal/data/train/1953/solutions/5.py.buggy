# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def removeNthFromEnd(self, head, n):
         positions = {}
         cur = head
         i = 0
         while cur:
             i += 1
             positions[i] = cur
             cur = cur.next
         
         if i == 1:
             return None
         elif n == i:
             return head.next
         else:
             parent = positions[i - n]
             toRemove = parent.next
             parent.next = toRemove.next
         
         return head
         
