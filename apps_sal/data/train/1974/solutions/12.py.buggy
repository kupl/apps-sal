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
         if not root:
             return []
 
         stack = [root]
         result = []
 
         while stack:
             node = stack.pop()
             if node.left or node.right:
                 stack.append(TreeNode(node.val))
                 if node.right:
                     stack.append(node.right)
                 if node.left:
                     stack.append(node.left)
             else:
                 result.append(node.val)
 
         return result        
