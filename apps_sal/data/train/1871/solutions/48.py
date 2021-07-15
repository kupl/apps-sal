# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = float(-inf)
        self.dfs(root, [])
        
        return self.res
    
    def dfs(self, node, path):
        if not node:
            self.res = max(self.res, max(path) - min(path))
            return
        
        self.dfs(node.left, path+[node.val])
        self.dfs(node.right, path+[node.val])

