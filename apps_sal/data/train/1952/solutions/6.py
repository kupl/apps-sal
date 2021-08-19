class Solution:

    def reverseBetween(self, head, m, n):
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        for i in range(m - 1):
            pre = pre.__next__
        cur = pre.__next__
        reverse = None
        for i in range(n - m + 1):
            next = cur.__next__
            cur.next = reverse
            reverse = cur
            cur = next
        pre.next.next = cur
        pre.next = reverse
        return dummyNode.__next__
        '\n         :type head: ListNode\n         :type m: int\n         :type n: int\n         :rtype: ListNode\n         '
