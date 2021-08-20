class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        (ans, stack) = ([], [])
        while head:
            while stack and stack[-1][1] < head.val:
                ans[stack.pop()[0]] = head.val
            stack.append([len(ans), head.val])
            ans.append(0)
            head = head.next
        return ans
