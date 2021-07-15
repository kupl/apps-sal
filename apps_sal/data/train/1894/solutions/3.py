# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def splitListToParts(self, root, k):
         """
         :type root: ListNode
         :type k: int
         :rtype: List[ListNode]
         """
         length = 0
         cur_node = root
         while cur_node:
             length += 1
             cur_node = cur_node.next
         result = []
         part_base_len = length // k
         p1 = length % k
         p0 = k - p1
         cur_node = root
         for i in range(p1):
             head = None
             c_node = None
             for j in range(part_base_len + 1):
                 if not head:
                     head = ListNode(cur_node.val)
                     c_node = head
                 else:
                     c_node.next = ListNode(cur_node.val)
                     c_node = c_node.next
                 cur_node = cur_node.next
             result.append(head)
         for i in range(p0):
             if cur_node:
                 head = None
                 c_node = None
                 for j in range(part_base_len):
                     if cur_node:
                         if not head:
                             head = ListNode(cur_node.val)
                             c_node = head
                         else:
                             c_node.next = ListNode(cur_node.val)
                             c_node = c_node.next
                         cur_node = cur_node.next
                 result.append(head)
             else:
                 result.append([])
         return result
