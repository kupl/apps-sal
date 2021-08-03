# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def rob(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if not root:
             return 0
         
         dp = {}
         
         def rob1(node):
             if node.left and node.left not in dp:
                 dp[node.left] = rob1(node.left)
             if node.right and node.right not in dp:
                 dp[node.right] = rob1(node.right)
             
             temp = node.val
 
             if node.left and node.left.left:
                 temp += dp[node.left.left]
             if node.left and node.left.right:
                 temp += dp[node.left.right]
             if node.right and node.right.left:
                 temp += dp[node.right.left]
             if node.right and node.right.right:
                 temp += dp[node.right.right]
             
             t = 0
             if node.left:
                 t += dp[node.left]
             if node.right:
                 t += dp[node.right]
             
             return max(t, temp)
         
         return rob1(root)
         
