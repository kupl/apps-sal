class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        p = head
        prev = None
        while p:
            q = p.__next__
            s = p.val
            while q and s:
                s += q.val
                q = q.__next__
            if s == 0:
                if p == head:
                    p = q
                    head = q
                else:
                    prev.next = q
                p = q
            else:
                prev = p
                p = p.__next__
        return head
