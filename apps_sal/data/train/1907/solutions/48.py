# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         def find(orig, copy, target):
#             if not orig: return None
#             if orig == target: return copy
#             return find(orig.left, copy.left, target) or find(orig.right, copy.right, target)
            
#         return find(original, cloned, target)

        def it(node):
            if node:
                yield node
                yield from it(node.left)
                yield from it(node.right)
        for n1, n2 in zip(it(original), it(cloned)):
            if n1 == target:
                return n2
