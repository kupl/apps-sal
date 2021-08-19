# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        def lreverse(head):
            if head is None:
                return head
            p = None
            q = head
            r = head.__next__
            while q:
                q.next = p
                p = q
                q = r
                if r:
                    r = r.__next__
            return p
        head = lreverse(head)
        q, res = [], []
        while head:
            while q and head.val >= q[-1]:
                q.pop()
            if len(q) == 0:
                res.append(0)
            else:
                res.append(q[-1])
            q.append(head.val)
            head = head.__next__

        return res[::-1]
