# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned.val == target.val:
            return cloned
        if cloned.left:
            node = self.getTargetCopy(original,cloned.left,target)
            if node:
                return node
        if cloned.right:
            node = self.getTargetCopy(original,cloned.right,target)
            if node:
                return node
        return None
        
            
            

