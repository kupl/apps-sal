class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stk = []
        ans = []
        i = 0
        while head:
            ans.append(0)
            stk.append((i, head.val))
            while head.next and stk and (head.next.val > stk[-1][1]):
                (j, _) = stk.pop()
                ans[j] = head.next.val
            head = head.next
            i += 1
        return ans
