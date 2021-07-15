# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 from collections import OrderedDict
 
 class Solution:
     def deleteDuplicates(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
         lookup = OrderedDict()
         
         while head:
             if head.val in lookup:
                 lookup[head.val] += 1
             else:
                 lookup[head.val] = 1
             head = head.next
         
         previous = None
         head = None
         for key in lookup:
             
             if (lookup[key] != 1):
                 continue
                 
             node = ListNode(key)
             if previous:
                 previous.next = node
             else:
                 head = node
             previous = node
 
         return(head)
         
         
