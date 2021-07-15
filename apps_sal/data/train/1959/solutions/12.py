# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         tree = []
         
         def Traversal(node):
             if node != None:
                 Traversal(node.left)
                 tree.append(node.val)
                 Traversal(node.right)
                 
         Traversal(root)
         
         mini = float('inf')
         for i in range(1, len(tree)):
             if abs(tree[i-1]-tree[i]) < mini:
                 mini = abs(tree[i-1]-tree[i])
         return mini
