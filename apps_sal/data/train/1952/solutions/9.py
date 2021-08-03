class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        h = ListNode(0)
        h.next = head
        count = 0
        cur = h
        leftPrev = None
        prev = None
        right = None
        while cur:
            if count == m:
                leftPrev = prev
                left = cur
            if count == n:
                right = cur
                break
            count += 1
            prev = cur
            cur = cur.__next__
        if leftPrev == None or left == right:
            return h.__next__
        rightNext = right.__next__
        tail = right.__next__
        cur = left
        while cur != rightNext:
            temp = cur
            cur = cur.__next__
            temp.next = tail
            tail = temp
        leftPrev.next = tail
        return h.__next__
