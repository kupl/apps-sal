# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#   1
# /   \\
# 2    3

# [1, 2,null, null,3, null, null]

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
      return self.helper(root)[0]
        
    def helper(self, root):
        if not root:
            return None, 0
        n1, l1 = self.helper(root.left)
        n2, l2 = self.helper(root.right)

        if l1 > l2:
            return n1, l1+1
        elif l1 < l2:
            return n2, l2+1
        else:
            return root, l1+1

