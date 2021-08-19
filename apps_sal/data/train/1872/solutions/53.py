class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root]
        max_sum = float('-inf')
        max_level = 0
        level = 0
        while len(queue) > 0:
            level_length = len(queue)
            level_sum = 0
            for i in range(level_length):
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if max_sum < level_sum:
                max_sum = level_sum
                max_level = level + 1
            level += 1
        return max_level
