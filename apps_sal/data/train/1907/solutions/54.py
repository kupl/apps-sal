# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def it(node):
            if node:
                yield node
                yield from it(node.left)
                yield from it(node.right)
                
        for a, b in zip(it(original), it(cloned)):
            if a == target:
                return b
