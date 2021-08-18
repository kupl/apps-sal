class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ans = []
        stack = []

        while head:
            while stack and stack[-1][0] < head.val:
                ans[stack.pop()[1]] = head.val
            stack.append((head.val, len(ans)))
            ans.append(0)
            head = head.next
        return ans
