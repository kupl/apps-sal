# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def zigzagLevelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         from collections import deque
         mydeque = deque()
         ret = []
         if root == None:
             return []
         mydeque.append(root)
         reverseflag = False
         while len(mydeque) != 0:
             curlist = []
             newdeque = deque()
             width = len(mydeque)
             for _ in range(0, width):
                 node = mydeque.pop()
                 if reverseflag:
                     node.left, node.right = node.right, node.left
                 curlist.append(node.val)
                 if node.left != None:
                     newdeque.append(node.left)
                 if node.right != None:
                     newdeque.append(node.right)
             mydeque = newdeque
             ret.append(curlist)
             reverseflag = not reverseflag
         return ret
