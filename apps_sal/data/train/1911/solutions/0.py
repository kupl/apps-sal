# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def sortList(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
         arr = []
         p = head
         while p:
             arr.append(p.val)
             p = p.next
             
         arr.sort()
         p = head
         for el in arr:
             p.val = el
             p = p.next
         
         return head
