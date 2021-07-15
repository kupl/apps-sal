# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def removeNthFromEnd(self, head, n):
         """
         :type head: ListNode
         :type n: int
         :rtype: ListNode
         """
         dummy = ListNode(0)
         dummy.next = head
         slow = fast = dummy
 
         for _ in range(n):
             fast = fast.next
 
         while fast.next != None:
             fast = fast.next
             slow = slow.next
 
         slow.next = slow.next.next
         temp = dummy.next
         while temp != None:
             print(temp.val)
             temp = temp.next
         return dummy.next
