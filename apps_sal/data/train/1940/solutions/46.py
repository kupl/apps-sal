class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        dic = {}
        stack = []
        i = 0
        ans = [0] * 100001
        while head:
            while stack and dic[stack[-1]] < head.val:
                t = stack.pop()
                ans[t] = head.val
            dic[i] = head.val
            stack.append(i)
            i += 1
            head = head.__next__
        while stack:
            t = stack.pop()
            ans[t] = 0
        return ans[:i]
