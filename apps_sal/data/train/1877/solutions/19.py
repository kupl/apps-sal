# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
 
        
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, path_sum):
            # parent has one child
            if not node:
                return False
            path_sum += node.val
            # if leaf
            if not node.left and not node.right:
                return path_sum >= limit
            left = dfs(node.left, path_sum)
            right = dfs(node.right, path_sum)
            # delete here itself
            if not left:
                node.left = None
            if not right:
                node.right = None
            return left or right
        result = dfs(root, 0)
        return root if result else None
        
        
        
        
        
        
            

