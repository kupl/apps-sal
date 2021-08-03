# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def deleteDuplicates(self, head):
         temp = head
         res = None
         resHead = None
         counter = 0
 
         while temp != None:
             counter = counter + 1
             if temp.next != None and temp.val == (temp.next).val:
                 duplicateval = temp.val
                 print("Duplicate Val: %d" % duplicateval)
 
                 # Iterate through the list till the value of duplicate are ongoing
                 while temp != None and temp.val == duplicateval:
                     temp = temp.next
             else:
                 if res == None:
                     res = ListNode(0)
                     res.val = temp.val
                     res.next = None
                     resHead = res
                 else:
                     res = resHead
                     while res.next != None:
                         res = res.next
                     
                     res.next = ListNode(0)
                     (res.next).val = temp.val
                     (res.next).next = None
             
                 temp = temp.next
                 #print("Next: %d", temp.val)
             
         return resHead
