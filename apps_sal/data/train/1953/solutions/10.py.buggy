# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 #[]
 #[1]
 class Solution:
     def removeNthFromEnd(self, head, n):
         """
         :type head: ListNode
         :type n: int
         :rtype: ListNode
         """
         if not head.next:
             return []
 
         dummy=ListNode(None)
         pre=ListNode(None)
         dummy.next=head
         pre.next=head
         count=1
         while head.next:
             if count<n:
                 count+=1
                 head=head.next
             else:
                 pre=pre.next
                 count-=1 
         if pre.val==None:
             return dummy.next.next
         else:
             pre.next=pre.next.next
             return dummy.next
                 
             
         
