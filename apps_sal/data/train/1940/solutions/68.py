class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        cur = head
        res = [0] * 1000000
        ind = 0

        while cur:

            while stack and stack[-1][1] < cur.val:
                res[stack[-1][0]] = cur.val
                stack.pop()

            stack.append((ind, cur.val))
            ind += 1
            cur = cur.__next__

        return res[:ind]
