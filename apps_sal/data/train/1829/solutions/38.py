# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check(node,val):
            if not node:
                return 0
            if node.val>=val:
                return 1 + check(node.left,node.val) + check(node.right,node.val)
            return check(node.left,val) + check(node.right,val)
        return check(root,root.val)
