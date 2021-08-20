class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        curr_level = max_level = 1
        max_sum = float('-inf')
        queue = [root]
        while queue:
            curr_sum = sum([x.val for x in queue])
            if curr_sum > max_sum:
                (max_sum, max_level) = (curr_sum, curr_level)
            queue = [y for x in queue for y in [x.left, x.right] if y]
            curr_level += 1
        return max_level
