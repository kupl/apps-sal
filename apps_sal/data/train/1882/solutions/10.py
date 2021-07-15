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
         
         if head is None:
             return []
         elif head.next is None:
             return head
         
         itr1 = head
         itr2 = head.next
         prev = itr1
         head = itr2
         d = head
         
         while itr1 is not None and itr2 is not None:
             temp = itr2.next
             itr2.next = itr1
             itr1.next = temp
             itr1 = itr1.next
             if itr1 is not None:
                 itr2 = itr1.next
                 if itr2 is None:
                     prev.next = itr1
                 else:
                     prev.next = itr2
                 prev = itr1
 
 
             print("=========")
             
             while d is not None:
                 print(d.val)
                 d = d.next
             d = head
             print("===========")
             
 
             
         return head
