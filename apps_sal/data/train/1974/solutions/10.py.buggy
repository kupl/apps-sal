# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def postorderTraversal(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         res,stack=[],[(root,False)]
         while stack:
             node,flag=stack.pop()
             if node:
                 if flag:
                     res.append(node.val)
                 else:
                     stack.append((node,True))
                     stack.append((node.right,False))
                     stack.append((node.left,False))
         return res
         
