# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def getnode(root):
            if not root:
                return None
            elif root.val == target.val:
                return root
            else:
                return getnode(root.left) or getnode(root.right)
        return getnode(cloned)
