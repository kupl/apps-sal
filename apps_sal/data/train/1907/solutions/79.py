# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(original, cloned, target):
            if original is None:
                return False
            
            if original.val == target.val:
                return cloned
            
            left = dfs(original.left, cloned.left, target)
            right = dfs(original.right, cloned.right, target)
            print(left, right)
            if left:
                return left
            if right:
                return right
            
        return dfs(original, cloned, target)
