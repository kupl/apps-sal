# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return None
        if cloned.val == target.val:
            return cloned
        a = self.getTargetCopy(original.left, cloned.left, target)
        b = self.getTargetCopy(original.right, cloned.right, target)
        if a is not None:
            return a
        if b is not None:
            return b
        return None
