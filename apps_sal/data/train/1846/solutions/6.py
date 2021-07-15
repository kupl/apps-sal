# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)
    
    def dfs(self, root):
        if not root:
            return None
        
        root.left = self.dfs(root.left)
        root.right = self.dfs(root.right)
        
        # Bubble up None
        if not root.val and not root.left and not root.right:
            return None
        
        return root
        

