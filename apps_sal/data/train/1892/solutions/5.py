# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def pathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         result = []
         def helper(root,target,sum,cur_result):
             if not root:
                 return
             target-=root.val
             cur_result.append(root.val)
             if target == 0 and not root.left and not root.right:
                 result.append([i for i in cur_result])
             helper(root.left,target,sum,cur_result)    
             helper(root.right,target,sum,cur_result)    
             cur_result.pop()
         helper(root,sum,0,[])    
         return result 
