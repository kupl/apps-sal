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
         previous_node, current_node = None, head
         ret = self.getKElem(head, k - 1)
         if not ret: return head
         last = ret
         while last:
             if previous_node: previous_node.next = last
             for _ in range(k):
                 next_node = current_node.next
                 current_node.next = previous_node
                 current_node, previous_node = next_node, current_node
             previous_node = head
             previous_node.next = current_node
             head = current_node
             last = self.getKElem(head, k - 1)
         
         return ret
     
     def getKElem(self, head, k):
         if k < 0: return None
         while k > 0:
             if not head: return None
             k -= 1
             head = head.next
         return head
