# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
 
 class Solution(object):
     def deleteDuplicates(self, head):
         """
         :type head: ListNode
         :rtype: ListNode
         """
         #start from nothing so we don't need to invalidate our position later
         real_head = ListNode(0)
         #previous also points to nothing at the start
         previous, current = real_head, head
         while current:
             #validate current.next OTHERWISE IT CRAHES DUMMY
             if current.next and current.next.val == current.val:
                 #remove ALL of the value in a tight loop
                 val_remove = current.val;
                 while current and current.val == val_remove:
                     current = current.next
                 previous.next = current
             else:
                 previous.next = current
                 previous = current
                 current = current.next
         return real_head.next
             
         
