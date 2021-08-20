class Solution:

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        count = 0
        pre = dummy
        while head:
            count += 1
            temp = head.next
            if count == m:
                mNode = head
            if count < m:
                pre = pre.next
            if count > m and count <= n:
                head.next = pre.next
                pre.next = head
                mNode.next = temp
            head = temp
        return dummy.next
