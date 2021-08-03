# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def kthSmallest(self, root, k):
         """
         :type root: TreeNode
         :type k: int
         :rtype: int
         """
         if root == None:
             return None
         else:
             node = root
             visited = []
             count = 0
             while node or visited:
                 if node:
                     visited.append(node)
                     node = node.left
                 else:
                     cur = visited.pop()
                     count = count+1
                     if count == k:
                         return cur.val
                     else:
                         node = cur.right
             return None
         
