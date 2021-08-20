class Solution:

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n == m:
            return head
        pre_head = head
        re_tail = head
        for i in range(m - 1):
            pre_head = re_tail
            re_tail = pre_head.__next__
        tmp_head = re_tail
        new_head = None
        for i in range(n - m + 1):
            next_node = tmp_head.__next__
            tmp_head.next = new_head
            new_head = tmp_head
            tmp_head = next_node
        re_tail.next = tmp_head
        if m == 1:
            return new_head
        else:
            pre_head.next = new_head
            return head
