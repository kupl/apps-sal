# Definition for a binary tree node.
 # class TreeNode(object):
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution(object):
     def printTree(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[str]]
         """
         if not root:
             return []
         
         if root.left is root.right:
             return [[str(root.val)]]
         
         def mydepth(root):
             return max(mydepth(root.left), mydepth(root.right)) + 1 if root else 0
         
         depth = mydepth(root)
         n = 2 ** depth - 1
         ans = [["" for _ in range(n)] for _ in range(depth)]
         
         def dfs(root, currdepth, distance):
             if not root:
                 return 
             
             ans[currdepth][distance] = str(root.val)
             
             dfs(root.left, currdepth + 1, distance - 2 ** (depth - 2 - currdepth))
             dfs(root.right, currdepth + 1, distance +  2 ** (depth - 2 - currdepth))
             
         
         dfs(root, 0, 2 ** (depth - 1) - 1)
         return ans
             
