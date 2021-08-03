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
         i=0
         node=head
         while(node):
             i=i+1
             if(node.next):
                 node=node.next
             else:
                 break
         num=i-n
         if(num==0):
             return head.next
         
         cur=head
         for k in range(num-1):
             cur=cur.next
         cur.next=cur.next.next
         return head
