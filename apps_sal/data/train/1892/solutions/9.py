# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def pathSum(self, root, sums):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         self.ret = []
         def dfs(root, s, path):
             if root.left is None and root.right is None:
                 if s == sums:
                     self.ret.append(path)
                 return
             if root.left:
                 dfs(root.left, s+root.left.val, path + [root.left.val])
             if root.right:
                 dfs(root.right, s+root.right.val, path + [root.right.val])
         if not root:return []
         dfs(root, root.val, [root.val])
         return self.ret

