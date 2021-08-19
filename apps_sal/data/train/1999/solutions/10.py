class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        m = {0: (dummy, 0)}
        cur_sum = cur = 0
        A = []

        def check(i, A):
            return all((not s < i <= e for (s, e) in A))
        while head:
            cur_sum += head.val
            cur += 1
            if cur_sum in m:
                i = m[cur_sum][1]
                if check(i, A):
                    m[cur_sum][0].next = head.next
                    A.append((i, cur))
                else:
                    m[cur_sum] = (head, cur)
            else:
                m[cur_sum] = (head, cur)
            head = head.next
        return dummy.next
