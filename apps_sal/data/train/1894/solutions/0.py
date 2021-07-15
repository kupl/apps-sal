# Definition for singly-linked list.
 # class ListNode(object):
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution(object):
     def splitListToParts(self, root, k):
         """
         :type root: ListNode
         :type k: int
         :rtype: List[ListNode]
         """
         if not root:
             return [None for _ in range(k)]
         
         if k == 1:
             return [root]
         
         count_nodes = 1
         start = root
         while start.next:
             start = start.next
             count_nodes += 1
         
         buckets = [0 for _ in range(k)]
         for i in range(len(buckets)):
             import math
             
             curr = math.ceil(count_nodes / k)
             count_nodes -= curr
             k -= 1
             buckets[i] = curr
             
             if count_nodes == 0:
                 break
 
         def split_ll(root, result, index, buckets):
             if index == len(buckets):
                 return
             if not root:
                 result.append(None)
                 return split_ll(root, result, index + 1, buckets)
             
             end = root
             curr_count = 1
             while curr_count < buckets[index]:
                 end = end.next
                 curr_count += 1
             
             start = root
             root = end.next
             end.next = None
             
             result.append(start)
             return split_ll(root, result, index + 1, buckets)
         
         result = []
         split_ll(root, result, 0, buckets)
         return result
             

