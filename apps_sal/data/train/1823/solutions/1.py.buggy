# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def reorderList(self, head):
         """
         :type head: ListNode
         :rtype: void Do not return anything, modify head in-place instead.
         """
         if not head:
             return None
         fast = slow = head
         temp = ListNode(0)
         while fast and fast.next:
             slow = slow.next
             fast = fast.next.next
         node = slow.next
         slow.next = None
         pre = None
         while node:
             cur = node.next
             node.next = pre
             pre = node
             node = cur
         first = head
         second = pre
         while first and second:
             node = first.next
             first.next = second
             second = second.next
             first.next.next = node
             first = node

