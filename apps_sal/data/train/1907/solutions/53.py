# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def lis(root):
            if root:
                yield root
                yield from lis(root.left)
                yield from lis(root.right)
                
        for a,b in zip(lis(original),lis(cloned)):
            if a==target:
                return b
