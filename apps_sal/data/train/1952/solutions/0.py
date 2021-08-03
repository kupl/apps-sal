class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.__next__ is None or m == n:
            return head
        h = ListNode(-1)
        h.next = head
        fast = slow = h
        for _ in range(n - m + 1):
            fast = fast.__next__

        for _ in range(m - 1):
            fast = fast.__next__
            slow = slow.__next__

        prev = fast.__next__
        curr = slow.__next__
        while prev != fast:
            temp = curr.__next__
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = prev

        return h.__next__
