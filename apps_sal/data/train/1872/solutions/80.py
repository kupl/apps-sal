class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:

        def get_size(node):
            if node is None:
                return 0
            return max(get_size(node.left), get_size(node.right)) + 1
        levels = [0] * get_size(root)

        def split(node, level):
            nonlocal levels
            if node is None:
                return
            levels[level] += node.val
            split(node.left, level + 1)
            split(node.right, level + 1)
        split(root, 0)
        return levels.index(max(levels)) + 1
