# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def swapPairs(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
         guard = ListNode(0)
         guard.next = head
         prev = guard
         cur = head
         while cur != None and cur.next != None:
             nxt = cur.next
             print(prev.val, cur.val, nxt.val)
             # do swap
             cur.next = nxt.next
             nxt.next = cur
             prev.next = nxt
             # move forward
             prev = cur
             cur = cur.next
             
             tmp = guard
             while tmp:
                 print(tmp.val)
                 tmp = tmp.next
         return guard.next
         
