from collections import namedtuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


leaf_info = namedtuple(\"Leaf_Info\", \"depth sum\")


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        def leaves(node: TreeNode, depth: int, path_sum: int) -> leaf_info:
            if node is None:
                yield leaf_info(0, 0)
            elif is_leaf(node):
                yield leaf_info(depth, node.val)
            else:
                yield from leaves(node.left, depth + 1, path_sum)
                yield from leaves(node.right, depth + 1, path_sum)
        
        max_depth = 0
        leaves_sum = 0
        for leaf in leaves(root, 0, 0):
            if leaf.depth > max_depth:
                max_depth, leaves_sum = leaf
            elif leaf.depth == max_depth:
                leaves_sum += leaf.sum

        return leaves_sum

