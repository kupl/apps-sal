# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ol = self.toList(original)
        cl = self. toList(cloned)
        index = ol.index(target)
        return cl[index]

    def toList(self, root: TreeNode):
        if root is None:
            return []
        return self.toList(root.left) + [root] + self.toList(root.right)
