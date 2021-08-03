# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def pathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         curr_path = []
         if root == None:
             return curr_path
         else:
             return self.pathSumHelper(root, sum, curr_path)
         
     def pathSumHelper(self, root, sum, curr_path):
         new_path = curr_path + [root.val]
         if root.left is None and root.right is None:
             return [new_path] if sum == root.val else []
         elif root.left is None:
             return self.pathSumHelper(root.right, sum - root.val, new_path)
         elif root.right is None:
             return self.pathSumHelper(root.left, sum - root.val, new_path)
         else:
             return self.pathSumHelper(root.right, sum - root.val, new_path) + self.pathSumHelper(root.left, sum - root.val, new_path)
