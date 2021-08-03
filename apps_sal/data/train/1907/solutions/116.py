# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # n=n=n=n=n=n=n=
    def getTargetCopy(self, p: TreeNode, q: TreeNode, target: TreeNode) -> TreeNode:
        if not p and not q:
            return
        if p == target:
            return q
        return self.getTargetCopy(p.left, q.left, target) or self.getTargetCopy(p.right, q.right, target)
