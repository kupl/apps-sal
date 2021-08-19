# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def search(root, val):
            if root is None:
                return None

            if root.val == val:
                return root

            return search(root.left, val) or search(root.right, val)

        if original is None:
            return None

        return search(cloned, target.val)
