# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # unique node val
        
        q = Queue()
        q.put(cloned)
        
        while q.qsize():
            node = q.get()
            
            if node.val == target.val:
                return node
            
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
