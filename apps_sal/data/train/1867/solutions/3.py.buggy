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
         cur = root
         stack = []
         count = 0
         while(len(stack) > 0 or cur):
             while(cur):
                 stack.append(cur)
                 cur = cur.left
             tmp = stack.pop()
             count += 1
             if(count == k): return tmp.val
             cur = tmp.right
         return -1
