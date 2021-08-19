# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        tot, cur = 0, head
        while cur:
            tot += cur.val
            cur = cur.__next__
            if tot == 0:
                return self.removeZeroSumSublists(cur)
        head.next = self.removeZeroSumSublists(head.next)
        return head
