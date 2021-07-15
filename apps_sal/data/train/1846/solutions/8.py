# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        return root if self.dfs(root) else None
    
    def dfs(self, root):
        if not root:
            return False
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if not l:
            root.left = None
        if not r:
            root.right = None
        return root.val == 1 or l or r
