# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def splitBST(self, root, V):
         left_bucket = []
         right_bucket = []
         
         def explore(node, V):
             if not node:
                 return
             
             if node.val <= V:
                 left_bucket.append(node)
                 explore(node.right, V)
                 node.right = None
             else:
                 right_bucket.append(node)
                 explore(node.left, V)
                 node.left = None
         
         explore(root, V)
         
         for i in range(1, len(left_bucket)):
             parent = left_bucket[i-1]
             child = left_bucket[i]
             if child.val <= parent.val:
                 parent.left = child
             else:
                 parent.right = child
         
         for i in range(1, len(right_bucket)):
             parent = right_bucket[i-1]
             child = right_bucket[i]
             if child.val <= parent.val:
                 parent.left = child
             else:
                 parent.right = child 
                 
         left = None
         
         if len(left_bucket) > 0:
             left = left_bucket[0]
         right = None
         if len(right_bucket) > 0:
             right = right_bucket[0]
         
         return [left, right]
         
         """
         :type root: TreeNode
         :type V: int
         :rtype: List[TreeNode]
         """
         
