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
         if head == None:
             return None
         if k == 1:
             return head
         res = []
         while(head!=None):
             res.append(head.val)
             head = head.next
         lens = len(res)
         res1 = []
         start = 0
         while(start+k <= lens):
             b = res[start:start+k]
             c = list(reversed(b))
             res1 += c
             start += k
         b = res[start:lens]
         res1 += b
         return res1
         
         
