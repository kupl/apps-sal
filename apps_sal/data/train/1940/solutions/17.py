from collections import deque


class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        while head != None:
            res.append(head.val)
            head = head.__next__
        stack = deque()
        for i in range(len(res)):
            while stack:
                if res[stack[-1]] < res[i]:
                    pos = stack.pop()
                    res[pos] = res[i]
                else:
                    break
            stack.append(i)
        while stack:
            pos = stack.pop()
            res[pos] = 0
        return res
