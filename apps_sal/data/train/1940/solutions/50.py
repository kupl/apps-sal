class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []

        stack = []
        res = []

        idx = 0
        while head:
            while stack and stack[-1][1] < head.val:
                pos, _ = stack.pop()
                res[pos] = head.val
            stack.append((idx, head.val))
            res.append(0)
            idx += 1
            head = head.next

        return res
