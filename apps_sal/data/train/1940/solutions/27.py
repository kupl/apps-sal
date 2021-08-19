class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        (res, stack) = ([], [])
        while head:
            while stack and stack[-1][1] < head.val:
                top = stack.pop()
                res[top[0]] = head.val
            stack.append([len(res), head.val])
            res.append(0)
            head = head.__next__
        return res
