# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = []
        stackCloned = []
        while stack or original.left or original.right:
            while original:
                if original is target:
                    return(cloned)
                if original.right:
                    stack.append(original.right)
                    stackCloned.append(cloned.right)                    
                original = original.left
                cloned = cloned.left
            original = stack.pop()
            cloned = stackCloned.pop()
        if original is target:
            return(cloned)
