class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        map = {}
        stack = []
        for (i, x) in enumerate(nums):
            while stack and stack[-1][1] < x:
                map[stack.pop()[0]] = x
            stack.append((i, x))
        res = []
        for (i, x) in enumerate(nums):
            res.append(map.setdefault(i, 0))
        return res
