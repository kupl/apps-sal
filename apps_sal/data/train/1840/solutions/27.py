class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        (*_, max_depth) = self.zigzag(root)
        return max_depth

    def zigzag(self, node: TreeNode) -> int:
        if node is None:
            return (-1, -1, 0)
        (_, left_depth, left_max) = self.zigzag(node.left)
        (right_depth, _, right_max) = self.zigzag(node.right)
        left_depth += 1
        right_depth += 1
        max_depth = max(left_depth, right_depth, left_max, right_max)
        return (left_depth, right_depth, max_depth)
