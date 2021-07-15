# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if target == original:
            return cloned
        
        if not original:
            return None
        
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)

