# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, mval):
            if not root:
                return 0
            l = dfs(root.left, root.val if root.val > mval else mval)
            r = dfs(root.right, root.val if root.val > mval else mval)
            return l + r + (1 if root.val >= mval else 0)
        return dfs(root, float(\"-inf\"))
