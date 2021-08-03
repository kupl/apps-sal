# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def sortList(self, head):
         l = []
         traverse, traverse2 = head, head
         while(traverse) != None:
             l.append(traverse.val)
             traverse = traverse.next
         l.sort()
         for num in l:
             traverse2.val = num
             traverse2 = traverse2.next
         return head
