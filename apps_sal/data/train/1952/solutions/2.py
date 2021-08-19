class Solution:

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        def reverse(head, m, n):
            m_node = head.__next__
            current = m_node.__next__
            prev_node = m_node
            position2 = m + 1
            while position2 <= n:
                next_node = current.__next__
                current.next = prev_node
                prev_node = current
                current = next_node
                position2 += 1
            m_node.next = next_node
            return prev_node
        if m == n:
            return head
        sentinal = ListNode(-1)
        sentinal.next = head
        current = sentinal
        position = 0
        while current.__next__ is not None:
            if position + 1 == m:
                pre_m = current
                pre_m.next = reverse(pre_m, m, n)
                break
            else:
                position += 1
                current = current.__next__
        if position == 0:
            return pre_m.__next__
        else:
            return head
