# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def generateSubTrees(self, left, right):
         ret = []
         if left >= right:
             ret.append(None)
         
         for i in range(left, right):
             left_sub_trees = self.generateSubTrees(left, i)
             right_sub_trees = self.generateSubTrees(i + 1, right)
             
             for left_tree in left_sub_trees:
                 for right_tree in right_sub_trees:
                     root = TreeNode(i)
                     root.left = left_tree
                     root.right = right_tree
                     ret.append(root)
         return ret
     
     def generateTrees(self, n):
         """
         :type n: int
         :rtype: List[TreeNode]
         """
         
         if n==0:
             return []
         return self.generateSubTrees(1, n+1)
             
