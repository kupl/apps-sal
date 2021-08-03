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
         def list_len(head):
             cnt = 0
             while head:
                 cnt += 1
                 head = head.next
             return cnt
         
         tlen = list_len(root)
         res = [None] * k
         if tlen <= k:
             i = 0
             head = root
             while head:
                 res[i] = head
                 i += 1
                 pre = head
                 head = head.next
                 pre.next = None
             return res
         
         rich = tlen % k
         h = tlen // k
         # print(tlen, k , rich, h)
         res[0] = root
 
         head = root
         cur = 1
         while cur < k:
             i = 1
             while i < h:
                 head = head.next
                 i += 1
             if rich > 0:
                 head = head.next
                 rich -= 1
             pre = head
             head = head.next
             res[cur] = head
             pre.next = None
             cur += 1
         return res
             
             
             
         
         
         
