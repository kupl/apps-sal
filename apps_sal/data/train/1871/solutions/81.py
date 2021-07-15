# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def visit(root, ancs):
            if root is None: return
            if ancs:
                self.ans = max(self.ans, max(abs(root.val - o) for o in ancs))
            visit(root.left, ancs+[root.val])
            visit(root.right, ancs+[root.val])
            
        visit(root, [])
        return self.ans
