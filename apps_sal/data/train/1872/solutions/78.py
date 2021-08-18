class Solution:
    import collections

    def maxLevelSum(self, root: TreeNode) -> int:
        levelSum = float('-inf')
        res = 0
        queue = collections.deque()
        queue.append((1, root))
        while len(queue) != 0:
            curr_sum = 0
            for _ in range(len(queue)):
                currl, curr = queue.popleft()
                curr_sum += curr.val
                if curr.left:
                    queue.append((currl + 1, curr.left))
                if curr.right:
                    queue.append((currl + 1, curr.right))
            if curr_sum > levelSum:
                res = currl
                levelSum = curr_sum
        return res
