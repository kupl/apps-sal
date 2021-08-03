# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.search(cloned, target)

    def search(self, node, target):
        if not node:
            return
        if node.val == target.val:
            return node
        return self.search(node.left, target) or self.search(node.right, target)
