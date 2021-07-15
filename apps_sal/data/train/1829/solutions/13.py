# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, float('-inf'))
        return self.count
    
    def dfs(self, root, parent):
        if not root:
            return 0
        
        if root.val >= parent:
            self.count += 1
        
        l = self.dfs(root.left, max(root.val, parent))

        r = self.dfs(root.right, max(root.val, parent))
        
        return l+r
            
                
                
            
            
        

