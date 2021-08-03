# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 import queue
 class Solution:
     def zigzagLevelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if root == None:
             return []
         bfs = queue.Queue()
         ret = []
         flag = 0
         bfs.put(root)
         
         while(bfs.empty()==False):
             cur_list = []
             bfs_len = bfs.qsize()
             for i in range(bfs_len):
                 cur = bfs.get()
                 if cur.left != None:
                     bfs.put(cur.left)
                 if cur.right != None:
                     bfs.put(cur.right)
                 cur_list.append(cur.val)
             if flag == 1:
                 cur_list.reverse()
                 flag = 0
             else:
                 flag = 1
             ret.append(cur_list)
         return ret
                 
         
