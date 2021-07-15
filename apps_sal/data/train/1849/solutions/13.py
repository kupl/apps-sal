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
         from queue import Queue
         
         q1, q2 = Queue(), Queue()
         q1.put(root)
         ret = []
         
         while (q1.empty() and not q2.empty()) or (not q1.empty() and q2.empty()):
             rst = []
             if not q1.empty():
                 # print("q1 not empty")
                 while not q1.empty():
                     node = q1.get()
                     if not node:
                         continue
                     else:
                         # print("q1:", node.val)
                         rst.append(node.val)
                         q2.put(node.left)
                         q2.put(node.right)
             else:
                 # print("q2 not empty")
                 while not q2.empty():
                     node = q2.get()
                     if not node:
                         continue
                     else:
                         # print("q2:", node.val)
                         rst.append(node.val)
                         q1.put(node.left)
                         q1.put(node.right) 
             if len(rst) > 0:
                 ret.append(rst)
         return ret
                 

