# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def removeNthFromEnd(self, head, n):
         """
         :type head: ListNode
         :type n: int
         :rtype: ListNode
         """
         
         ''' first trial. O(L) time, O(L) space complexity. 
         nodes_list = []
         cursor = head
         while cursor != None:
             nodes_list.append(cursor)
             cursor = cursor.next
         
         if n == len(nodes_list):
             head = head.next
         else :
             nodes_list[-n-1].next = nodes_list[-n].next
         
         return head
         '''
         
         # second trial after getting a hint from its solution.
         dummy = ListNode(0)
         dummy.next = head
         target_prev = dummy
         tail = head
         dist = 0
         while tail != None:
             if dist < n:
                 tail = tail.next
                 dist += 1
             else :
                 target_prev = target_prev.next
                 dist -= 1
         
         target_prev.next = target_prev.next.next
         return dummy.next
