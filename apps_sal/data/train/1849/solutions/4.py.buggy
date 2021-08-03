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
         if not root:
             return []
         q = [(0, root)]
         res = [[]]
         while q:
             level, node = q.pop()
             if level > len(res) - 1:
                 res.append([node.val])
             else:
                 res[level] += [node.val]
             if node.left:
                 q.insert(0,(level + 1, node.left))
             
             if node.right:
                 q.insert(0, (level + 1, node.right))
         return res
