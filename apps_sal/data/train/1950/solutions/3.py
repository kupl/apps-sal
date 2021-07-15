# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def deleteDuplicates(self, head):
         if head == None or head.next == None:
             return head 
        
         def get_next(node):
             while node != None and node.next != None and node.val == node.next.val:
                 cur_val = node.val
                 node = node.next.next
                 while node != None and node.val == cur_val:
                     node = node.next
             return node
 
         head = get_next(head)
         if head == None:
             return []
         
         prev = head
         cur = prev.next
         while (cur != None):
             cur = get_next(cur)
             prev.next = cur
             prev = cur
             if cur != None:
                 cur = cur.next
 
         return head
         
