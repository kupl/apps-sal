class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        temp = head
        while temp:
            s = 0
            start = temp
            while start:
                s += start.val
                if s == 0:
                    prev.next = start.__next__
                    break
                start = start.__next__
            if start == None:
                start = temp
                prev = temp
            temp = start.__next__
        return dummy.__next__
