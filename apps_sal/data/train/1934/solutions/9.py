# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 import queue
 class Solution:
     # # 用两个栈
     # def zigzagLevelOrder(self, root):
     #     """
     #     :type root: TreeNode
     #     :rtype: List[List[int]]
     #     """
     #     if (root is None):
     #         return []
     #     s1, s2 = [], []
     #     res = []
     #     level = []
     #     s1.append(root)
     #     deal_s1 = True
     #     while (s1 or s2):
     #         # 下面一行不能写成if(s1)，因为在处理s2时，会向s1中压数据
     #         if (deal_s1):
     #             cur = s1.pop()
     #             level.append(cur.val)
     #             if (cur.left is not None):
     #                 s2.append(cur.left)
     #             if (cur.right is not None):
     #                 s2.append(cur.right)
     #             if (not s1):
     #                 res.append(level[:])
     #                 level = []
     #                 deal_s1 = False
     #         else:
     #             cur = s2.pop()
     #             level.append(cur.val)
     #             if (cur.right is not None):
     #                 s1.append(cur.right)
     #             if (cur.left is not None):
     #                 s1.append(cur.left)
     #             if (not s2):
     #                 res.append(level[:])
     #                 level = []
     #                 deal_s1 = True
     #     return res
                 
     def zigzagLevelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if (root is None):
             return []
         res = []
         level = []
         q = queue.Queue()
         q.put(root)
         q.put(None)
         reverse = 1
         while (not q.empty()):
             cur = q.get()
             if (cur is None):
                 res.append(level[::reverse])
                 level = []
                 reverse *= -1
                 if (not q.empty()):
                     q.put(None)
             else:
                 level.append(cur.val)
                 if (cur.left is not None):
                     q.put(cur.left)
                 if (cur.right is not None):
                     q.put(cur.right)
         return res
         
