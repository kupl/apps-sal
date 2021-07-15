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
         if not root: return [None for _ in range(k)]
         length = 0;
         i = root;
         while i:
             i = i.next;
             length += 1;
             
         chunk_size = length//k
         num_longer_chunks = length % k
         
         res = [chunk_size + 1] * num_longer_chunks + [chunk_size] * (k - num_longer_chunks)
         
         curr = root;
         prev = None;
         
         for i,num in enumerate(res):
             res[i] = curr;
             for _ in range(num):
                 prev = curr;
                 curr = curr.next;
             
             prev.next = None;
             
         return res
         
