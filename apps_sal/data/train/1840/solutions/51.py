from typing import NamedTuple


class Result(NamedTuple):
    left_depth: int
    right_depth: int
    max_depth: int


class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        res = self.zigzag(root)
        return res.max_depth

    def zigzag(self, node: TreeNode) -> int:
        if node is None:
            return Result(-1, -1, 0)
        left_res = self.zigzag(node.left)
        right_res = self.zigzag(node.right)
        left_depth = left_res.right_depth + 1
        right_depth = right_res.left_depth + 1
        max_depth = max(left_depth, right_depth, left_res.max_depth, right_res.max_depth)
        return Result(left_depth, right_depth, max_depth)
