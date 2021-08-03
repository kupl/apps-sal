# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def reverseKGroup(self, head, k):
         """
         :type head: ListNode
         :type k: int
         :rtype: ListNode
         """
         root = p = ListNode(0);
         flag = 0
         while head:
             tlist = []
             for i in range(k):
                 if head != None:
                     tlist.append(head.val);
                     head = head.next;
                 else:
                     flag = 1;
                     break;
             if flag == 0:
                 for i in range(k):
                     p.next = ListNode(tlist[k-1-i]);
                     p = p.next;
             else:
                 for i in tlist:
                     p.next = ListNode(i);
                     p = p.next;
         return root.next
