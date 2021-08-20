class Solution:

    def longestZigZag(self, root: TreeNode) -> int:

        def zigzag(node: TreeNode) -> tuple:
            if not node:
                return (0, 0)
            (_, lr) = zigzag(node.left)
            (rl, _) = zigzag(node.right)
            self.max_path = max(self.max_path, lr + 1, rl + 1)
            return (lr + 1, rl + 1)
        self.max_path = 0
        zigzag(root)
        return self.max_path - 1
