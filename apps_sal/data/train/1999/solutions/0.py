class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        seen = {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        prev = 0
        while head:
            prev += head.val
            seen[prev] = head
            head = head.__next__
        head = dummy
        prev = 0
        while head:
            prev += head.val
            head.next = seen[prev].__next__
            head = head.__next__
        return dummy.__next__
