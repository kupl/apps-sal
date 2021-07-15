# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
 
 class Solution:
     def reverseKGroup(self, head, k):
         """
         :type head: ListNode
         :type k: int
         :rtype: ListNode
         """
 
         copy = head
         for _ in range(k):
             if copy is None:
                 return head
             else:
                 copy = copy.next
 
         k_nodes = []
         for _ in range(k):
             k_nodes.append(head)
             head = head.next
         rest = k_nodes[-1].next
 
         for i in reversed(range(1, len(k_nodes))):
             k_nodes[i].next = k_nodes[i-1]
         k_nodes[0].next = self.reverseKGroup(rest, k)
 
         return k_nodes[-1]
 

