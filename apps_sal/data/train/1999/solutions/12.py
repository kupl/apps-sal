# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = {}
        while cur:
            prefix += cur.val
            seen[prefix] = cur
            cur = cur.__next__
        cur = dummy
        prefix = 0
        while cur:
            prefix += cur.val
            cur.next = seen[prefix].__next__
            cur = cur.__next__
        return dummy.__next__
