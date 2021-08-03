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
         if head == None:
             return head
         
         i = head
         j = head.next
         k = None
         
         while i != None and j != None:
             
             i.next = j.next
             j.next = i
             
             if i == head:   # reposition head if we're at the front of the list
                 head = j
             
             if k:           # if we have a trailing node, link j into LL
                 k.next = j
                 
             # update node pointers
             if i.next != None:  
                 j = i.next.next 
                 k = i
             
             i = i.next
             
         return head
         
