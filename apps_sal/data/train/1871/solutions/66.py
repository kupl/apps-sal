# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from dataclasses import dataclass

MIN_VALUE = -2**31
MAX_VALUE = 2**31


@dataclass
class State:
    min_: int
    max_: int
    val: int


def max_ancestor_diff(root: TreeNode) -> State:
    if not root:
        return State(MAX_VALUE, MIN_VALUE, 0)
    
    left = max_ancestor_diff(root.left)
    right = max_ancestor_diff(root.right)
    
    min_ = min(left.min_, right.min_, root.val)
    max_ = max(left.max_, right.max_, root.val)
    val = max(left.val, right.val, max_ - root.val, root.val - min_)
    return State(min_, max_, val)
    

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return max_ancestor_diff(root).val

