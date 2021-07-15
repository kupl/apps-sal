# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        
        
        def dfs(original,cloned,target):
            if not original:
                return None
            # print(original.val)
            if original == target:
                # print('find')
                return cloned
            
            left = dfs(original.left,cloned.left,target)
            right = dfs(original.right,cloned.right,target)
            
            if left:
                return left
            else:
                return right
        result =  dfs(original,cloned,target)
        return result

