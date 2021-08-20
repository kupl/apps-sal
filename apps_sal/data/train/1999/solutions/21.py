class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        Head = ListNode(0)
        Head.next = head
        cur = Head
        while cur != None:
            sum = 0
            while head != None:
                sum = sum + head.val
                if sum == 0:
                    cur.next = head.__next__
                head = head.__next__
            cur = cur.__next__
            if cur != None:
                head = cur.__next__
        return Head.__next__
