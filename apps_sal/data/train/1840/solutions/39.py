# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0
        
        
        def dfs(node):
            # dfs(node) returns l, r
            # l means the longest zigzag path from node with the first edge going left
            # r means the longest zigzag path from node with the first edge going right
            if not node:
                return -1, -1
            _, r = dfs(node.left) # Note the the first returned value is useless
            l, _ = dfs(node.right)
            self.res = max(self.res, r + 1, l + 1)
            return r + 1, l + 1
        
        dfs(root)
        return self.res
