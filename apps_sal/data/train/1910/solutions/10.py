class Solution:

    def reverseKGroup(self, head, k):
        if not head:
            return head
        cur = head
        for _ in range(k - 1):
            cur = cur.next
            if not cur:
                return head
        prev = self.reverseKGroup(cur.next, k)
        cur.next = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            (prev, cur) = (cur, temp)
        return prev
