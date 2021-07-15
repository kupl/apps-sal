# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
\tdef lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
\t\treturn self.helper(root)[1]
\tdef helper(self,root):
\t\tif not root:
\t\t\treturn (0,None)
\t\tlevleft,lcal=self.helper(root.left)
\t\tlevright,lcar=self.helper(root.right)
\t\tif levleft>levright:
\t\t\treturn (levleft+1,lcal)
\t\telif levleft<levright:
\t\t\treturn (levright+1,lcar)
\t\treturn (levleft+1,root)
