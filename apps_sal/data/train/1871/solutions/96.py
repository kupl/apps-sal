from typing import List
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return max_ancestor_diff(root, [])


@lru_cache
def get_max_lineage_diff(node: TreeNode, lineage) -> int:
    if lineage:
        return max([abs(node.val - n.val) for n in lineage])
    else:
        return 0


def max_ancestor_diff(node: TreeNode, lineage: List[TreeNode]) -> int:
    if node is None:
        return 0

    max_diff = get_max_lineage_diff(node, frozenset(lineage))

    if node.left is not None:
        max_diff = max(max_diff, max_ancestor_diff(
            node.left, lineage + [node]))

    if node.right is not None:
        max_diff = max(max_diff, max_ancestor_diff(
            node.right, lineage + [node]))

    return max_diff
