# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.maxAncestorDiffHelper(root, [], 0)

    def maxAncestorDiffHelper(self, root: TreeNode, ancestors, maxV: int) -> int:
        if root is None:
            return 0
        for a in ancestors:
            maxV = max(maxV, abs(a - root.val))
        ancestors.append(root.val)
        maxV = max(
            maxV,
            self.maxAncestorDiffHelper(root.left, ancestors, maxV),
            self.maxAncestorDiffHelper(root.right, ancestors, maxV)
        )
        ancestors.pop()
        return maxV

    # TODO should be able to make this faster
