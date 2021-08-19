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
        if node == None:
            return None
        if node.val == target.val:
            return node
        n = self.search(node.left, target)
        if n:
            return n
        n = self.search(node.right, target)
        return n
