# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def sumNumbers(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if root is None:
             return 0
         ret = 0
         que = [root]
         while len(que) != 0:
             node = que.pop(0)
             if node.left is None and node.right is None:
                 ret += node.val
             if node.left:
                 node.left.val = node.val*10 + node.left.val
                 que.append(node.left)
             if node.right:
                 node.right.val = node.val*10 + node.right.val
                 que.append(node.right)
         return ret
         
