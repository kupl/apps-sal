# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def removeNthFromEnd(self, head, n):
         temp = head
         counter = 0
         while(temp!=None):
             counter += 1
             temp = temp.next
         timeToVisit = counter - n
         if timeToVisit == 0:
             return head.next
         if timeToVisit == 1:
             head.next = head.next.next
             return head
         nodeToDel = head
         while(timeToVisit>0):
             nodeToDel = nodeToDel.next
             timeToVisit -= 1
             if timeToVisit == 1:
                 nodeToSave = nodeToDel
                 nodeToNext = nodeToDel.next.next
                 nodeToSave.next = nodeToNext
         return head
         """
         :type head: ListNode
         :type n: int
         :rtype: ListNode
         """
         
