# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def getDepth(root):
            if not root:
                return 0
            left = getDepth(root.left)
            right = getDepth(root.right)
            return 1 + max(left, right)

        def getSubtrees(root):
            if root:

                leftDepth = getDepth(root.left)
                rightDepth = getDepth(root.right)
                if leftDepth == rightDepth:
                    return root
                elif leftDepth > rightDepth:
                    return getSubtrees(root.left)
                else:
                    return getSubtrees(root.right)

        return getSubtrees(root)
