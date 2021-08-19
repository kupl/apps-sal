# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        return self.traverse(original, cloned, target)

    def traverse(self, root: TreeNode, cloned: TreeNode, target: TreeNode):
        if root is None:
            return None
        elif root == target:
            return cloned
        left = self.traverse(root.left, cloned.left, target)
        if left:
            return left
        right = self.traverse(root.right, cloned.right, target)
        if right:
            return right
