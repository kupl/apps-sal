from collections import deque


class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        s = []
        cur = head
        while cur != None:
            if cur.val == 0:
                cur = cur.__next__
                continue
            back_sum = 0
            end_i = -1
            for i in range(len(s))[::-1]:
                back_sum += s[i].val
                if cur.val + back_sum == 0:
                    end_i = i
            if end_i != -1:
                for j in range(len(s) - 1, end_i - 1, -1):
                    s.pop()
            else:
                s.append(cur)
            cur = cur.__next__
        for i in range(len(s)):
            if i < len(s) - 1:
                s[i].next = s[i + 1]
            else:
                s[i].next = None
        if len(s) > 0:
            return s[0]
        else:
            return None
