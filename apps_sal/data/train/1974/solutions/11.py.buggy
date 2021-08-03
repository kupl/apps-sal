# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def postorderTraversal(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         res = []
         if not root:
             return res
         stack = []
         cur = root
         while cur or stack:
             while cur:
                 stack.append((cur, 0))
                 cur = cur.left
             node, flag = stack[-1]
             if flag:
                 node, _ = stack.pop()
                 res.append(node.val)
             else:
                 cur = node.right
                 stack[-1] = (node, 1)
         return res
