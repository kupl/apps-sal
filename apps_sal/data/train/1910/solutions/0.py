# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def kth(self, v, k):
         for i in range(k-1):
             if not v:
                 return None
             v=v.next
         return v
     
     def reverseKGroup(self, head, k):
         """
         :type head: ListNode
         :type k: int
         :rtype: ListNode
         """
         if k==1:
             return head
         kthnode=self.kth(head, k)
         v=head
         head=kthnode if kthnode else head
         i=0
         tmphead=v
         while kthnode:
             vprev=kthnode.next
             for i in range(k):
                 v.next, v, vprev = vprev, v.next, v
                 kthnode=None if not kthnode else kthnode.next
             tmphead.next=kthnode if kthnode else v
             tmphead=v
         return head
