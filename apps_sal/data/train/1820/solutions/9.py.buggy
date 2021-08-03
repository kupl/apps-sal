# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def largestValues(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         if not root:
             return []
         stack = []
         finallist = [root.val]
         if root.left:
             stack.append(root.left)
         if root.right:
             stack.append(root.right)
         
 
         while stack:
             #print(stack)
             temp = []
             maxval =-2147483648
             for node in stack:
                 #node = stack.pop()
                 maxval = max(maxval,node.val)
                 if node.right:
                     temp.append(node.right)
                 if node.left:
                     temp.append(node.left)
             
             finallist.append(maxval)
             stack = temp
             
         return finallist
                 
         
             
         
         
