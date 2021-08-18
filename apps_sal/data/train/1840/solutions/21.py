class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        _, max_depth = self.zigzag(root)
        return max_depth

    def zigzag(self, node: TreeNode, return_left=False) -> int:
        if node is None:
            return -1, 0
        left_depth, left_max = self.zigzag(node.left)
        right_depth, right_max = self.zigzag(node.right, return_left=True)

        left_depth += 1
        right_depth += 1
        max_depth = max(left_depth, right_depth, left_max, right_max)
        return left_depth if return_left else right_depth, max_depth
