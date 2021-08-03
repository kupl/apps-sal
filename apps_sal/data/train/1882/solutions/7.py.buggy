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
         root = p = ListNode(0);
         while head:
             a = head;
             if head.next:
                 b = head.next;
                 p.next = ListNode(b.val);
                 p = p.next;
                 p.next = ListNode(a.val);
                 p = p.next;
                 head = head.next.next;
             else:
                 p.next = ListNode(a.val);
                 head = a.next;
         return root.next
         
         
