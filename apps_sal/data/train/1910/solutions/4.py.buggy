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
         current = head 
         next  = None
         prev = None
         count = 0
         
         if(self.nextkthnode(head,k) is None):
             return head
         while(current is not None and count < k):
             next = current.next
             current.next = prev
             prev = current
             current = next
             count += 1
  
        
         if next is not None and self.nextkthnode(next,k) is not None:
             head.next = self.reverseKGroup(next, k)
         elif(next is not None):
             head.next = next
  
         return prev 
             
         
     def nextkthnode(self, head, k):
         for i in range(k-1):
             if(head==None):
                 return None
             head=head.next
         return head
