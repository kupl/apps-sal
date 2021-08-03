"""
 3->2->1->6->5->4
 
 """
 
 # Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 #return (head, tail)
 def reverse_LL2(node, length):
     if length == 1:
         return (node, node)
     back = None
     curr = node
     forward = node.next
     for _ in range(length):
         curr.next = back
         back = curr
         curr = forward
         if forward:
             forward = forward.next
     return (back, node)
 
 def reverse_LL(node, length):
     if length == 1:
         return node
     rest = node.next
     restR = reverse_LL(rest, length - 1)
     rest.next = node
     node.next = None
     return restR
     
     
 def jump_LL(node, length):
     curr = node
     for _ in range(length):
         if curr == None:
             return False
         curr = curr.next
     return curr
 
 class Solution:
     def reverseKGroup(self, head, k):
         if (head == None):
             return None
         jumped = jump_LL(head, k)
         if jumped == False:
             return head
         rev = reverse_LL(head, k)
         head.next = self.reverseKGroup(jumped, k)
         return rev
         
