class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        pos = 0
        ans = []
        stack = []
        while head:
            ans.append(0)
            while stack and stack[-1][1] < head.val:
                (idx, _) = stack.pop()
                ans[idx] = head.val
            stack.append((pos, head.val))
            head = head.next
            pos += 1
        return ans
