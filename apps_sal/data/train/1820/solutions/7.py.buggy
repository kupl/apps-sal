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
         level = []
         if root == None:
             return []
         level.append(root)
         ans = []
         
         while len(level) != 0:
             level_max = float("-inf")
             next_level = []
             while len(level) != 0:
                 cur_node = level.pop(0)
                 level_max = max(cur_node.val, level_max)
                 if cur_node.left != None:
                     next_level.append(cur_node.left)
                 if cur_node.right != None:
                     next_level.append(cur_node.right)
             ans.append(level_max)
             level = next_level
         return ans
         
         
