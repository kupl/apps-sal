# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_zigzag = 0
        
        def dfs(node):
            if not node:
                # [left, right, max]
                return [-1, -1, -1]
            left = dfs(node.left)
            right = dfs(node.right)
            return [left[1] + 1, right[0] + 1, max(left[2], right[2], left[1]+1, right[0]+1)]
        

        return dfs(root)[2]
    
        

