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
         if root == None:
             return []
         
         queue = collections.deque()
         
         reslist = []
         
         queue.append(root)
         
         while queue:
             level = []
             for i in range(len(queue)):
                 node = queue.popleft()
                 level.append(node.val)
                 if node.left != None:
                     queue.append(node.left)
                 if node.right != None:
                     queue.append(node.right)
             reslist.append(level)
         
         return reslist
