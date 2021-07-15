# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if root is None:
             return []
         vals = []
         self.traverse(root, vals, 0)
         return vals
         
     def traverse(self, node, vals, depth):
         if node is None:
             return
         self.traverse(node.left, vals, depth + 1)
         while len(vals) - 1 < depth:
             #print(depth)
             vals.append([])
         vals[depth].append(node.val)   
         self.traverse(node.right, vals, depth + 1)
         return
 
             
 
         
         
