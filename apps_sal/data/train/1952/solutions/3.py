class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n == 1:
            return head

        sentinel = ListNode(0)
        pre = sentinel
        pre.next = head
        end = head
        while m > 1:
            pre = pre.__next__
            m -= 1
        while n:
            end = end.__next__
            n -= 1
        new_start = self.reverse(pre.__next__, end)
        pre.next = new_start
        return sentinel.__next__

    def reverse(self, cur, end):
        new_head = end
        while cur != end:
            next = cur.__next__
            cur.next = new_head
            new_head = cur
            cur = next
        return new_head
