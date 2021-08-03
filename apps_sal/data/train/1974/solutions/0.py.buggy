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
         if root==None:
             return []
         stack=[]
         stack_left=[1]
         while stack_left!=[]:
             stack.append(root.val)
             if root.left!=None and root.right==None:
                 root=root.left
             elif root.left==None and root.right!=None:
                 root=root.right
             elif root.left!=None and root.right!=None:
                 stack_left.append(root.left)
                 root=root.right
             else:
                 if stack_left==[1]:
                     stack_left=[]
                 else:
                     root=stack_left.pop()
         #print(stack)
         stack.reverse()
         return stack
         
