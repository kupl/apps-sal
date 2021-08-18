
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')
        level = 0
        max_level = 0
        queue = []

        if not root:
            return 0

        queue.append(root)

        while len(queue) > 0:
            size = len(queue)
            level_sum = 0
            level += 1

            for i in range(size):
                node = queue.pop(0)
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if max_sum < level_sum:
                max_sum = level_sum
                max_level = level

        return max_level
