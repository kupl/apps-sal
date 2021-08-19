class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return [0]
        idx = -1
        res = []
        stack = []
        while head:
            res.append(0)
            while stack and stack[-1][1] < head.val:
                (position, _) = stack.pop()
                res[position] = head.val
            idx += 1
            stack.append((idx, head.val))
            head = head.__next__
        return res
