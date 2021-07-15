# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        maxlen = 0
        
        dt = collections.defaultdict(lambda : [0,0])
        
        def dfs(root,dt):
            nonlocal maxlen
            
            if root.left:
                dfs(root.left,dt)
                dt[root][0] = dt[root.left][1] + 1
            else:
                dt[root][0] = 0
                
            if root.right:
                dfs(root.right,dt)
                dt[root][1] = dt[root.right][0] + 1
            else:
                dt[root][1] = 0
            
            maxlen = max(maxlen, dt[root][0], dt[root][1])
            
        dfs(root,dt)
        
        return maxlen
        
                

