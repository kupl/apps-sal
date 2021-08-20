class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(float('inf'))
        dummy.next = head
        cur = head
        head = dummy
        while head:
            r_sum = 0
            while cur:
                r_sum += cur.val
                if r_sum == 0:
                    head.next = cur.__next__
                cur = cur.__next__
            head = head.__next__
            if head:
                cur = head.__next__
        return dummy.__next__
