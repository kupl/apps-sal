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
         stack_left = [1]
         stack = []
         while stack_left:
             stack.append(root.val)
             if not root.left and root.right:
                 root = root.right
             elif root.left and not root.right:
                 root = root.left
             elif root.left and root.right:
                 stack_left.append(root.left)
                 root = root.right
             else:
                 if stack_left == [1]:
                     stack_left = []
                 else:
                     root = stack_left.pop()
         stack.reverse()
         return stack
