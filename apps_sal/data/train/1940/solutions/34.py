class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        res = []
        pos = 0
        while head:
            res.append(0)
            while stack and head.val > stack[-1][1]:
                (idx, _) = stack.pop()
                res[idx] = head.val
            stack.append((pos, head.val))
            pos += 1
            head = head.next
        while stack:
            (idx, _) = stack.pop()
            res[idx] = 0
        return res
