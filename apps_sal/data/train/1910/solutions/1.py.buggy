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
         if head.next == None:
             return head
         
         cur = head
         prev = None
         count = 0
         if self.getsize(cur) >= k:
             while count < k and cur != None:
                 temp = cur
                 cur = cur.next
                 temp.next = prev
                 prev = temp
                 count = count + 1
             if cur != None:
                 head.next = self.reverseKGroup(cur, k)
             return prev
         
         return cur
                 
         
     def getsize(self, head):
         curnode = head
         count = 0
         while curnode != None:
             curnode = curnode.next
             count = count + 1
         return count
         
