# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def generateTrees(self, n):
         """
         :type n: int
         :rtype: List[TreeNode]
         """
         
         if n == 0:
             return []
         
         root_dict = dict()
         
         def recur(start, end):
             if start > end:
                 return [None]
             
             rl = root_dict.get((start, end))
             if not rl:
                 rl = []
                 for v in range(start, end+1):
                     for lc in recur(start, v-1):
                         for rc in recur(v+1, end):
                             root = TreeNode(v)
                             root.left, root.right = lc, rc
                             rl.append(root)
                             
                 root_dict[(start, end)] = rl
                 
             return rl
                         
         return recur(1, n)
                         
