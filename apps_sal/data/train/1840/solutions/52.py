# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.ret = 0
        self.dfs(root, 0, 0)
        self.dfs(root, 1, 0)
        return self.ret - 1
    
    def dfs(self, root, prevright, length):
        if root is None:
            self.ret = max(self.ret, length)
            return
        
        if prevright:
            self.dfs(root.left, 1 - prevright, length + 1)
            self.dfs(root.right, prevright, 1)
        else:
            self.dfs(root.right, 1 - prevright, length + 1)
            self.dfs(root.left, prevright, 1)
        
            
        return 
