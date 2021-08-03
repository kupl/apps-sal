# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 import queue
 class Solution:
     
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if root == None:
             return []
         ret = []
         bfs = []
         bfs.append(root)
         cur = 0
         nextl = len(bfs)
         
         while (cur<nextl):
             cur_level = []
             for i in range(cur,nextl):
                 cur_node = bfs[i]
                 if cur_node.left != None:
                     bfs.append(cur_node.left)
                 if cur_node.right != None:
                     bfs.append(cur_node.right)            
                 cur_level.append(bfs[i].val)
             ret.append(cur_level)
             cur,nextl = nextl, len(bfs)
         return ret
             
     
     
         
         
         
