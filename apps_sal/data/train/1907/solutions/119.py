# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def find(self, copy, target):
        
        if copy:
            if copy.val == target:
                return copy

            a = self.find(copy.left, target)
            return a if a else self.find(copy.right, target)
        return None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.find(cloned, target.val) 


