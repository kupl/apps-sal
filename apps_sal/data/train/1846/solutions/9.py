# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return False
            lone = helper(root.left)
            rone = helper(root.right)
            if not lone:
                root.left = None
            if not rone:
                root.right = None
            if root.val == 1 or lone or rone:
                return True
            else:
                return False

        if helper(root):
            return root
        else:
            return None
