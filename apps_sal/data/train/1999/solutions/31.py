class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        p = head
        nums = []
        while p:
            nums.append(p.val)
            p = p.__next__

        def check(nums):
            cur, k = 0, 0
            stack = []
            acc = [0] + list(accumulate(nums))
            for i, n in enumerate(nums):
                for j in range(k, i + 1):
                    if acc[i + 1] - acc[j] == 0:
                        stack.append((j, i))
                        k = i + 1
            return stack

        stack = check(nums)
        while stack:
            while stack:
                j, i = stack.pop()
                nums[j: i + 1] = []
            stack = check(nums)

        if not nums:
            return None
        ans = ListNode(nums[0])
        p = ans
        for i in range(1, len(nums)):
            p.next = ListNode(nums[i])
            p = p.__next__
        return ans
