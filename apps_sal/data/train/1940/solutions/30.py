class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        count = 0
        out = []
        while head:
            out.append(0)
            while stack and head.val > stack[-1][0]:
                out[stack[-1][1]] = head.val
                stack.pop()
            stack.append((head.val, count))
            count += 1
            head = head.__next__
        return out
