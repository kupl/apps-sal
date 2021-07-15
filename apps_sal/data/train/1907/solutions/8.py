# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def addToQueue(o_node, c_node, q, q_c):
            if o_node.val == target.val:
                return c_node
            q.put(o_node)
            q_c.put(c_node)
            return None
                
        if original is None or original.val == cloned.val == target.val:
            return cloned
        q = queue.Queue()
        q_c = queue.Queue()
        q.put(original)
        q_c.put(cloned)
        while not q.empty():
            o_node = q.get()
            c_node = q_c.get()
            if o_node.left and addToQueue(o_node.left, c_node.left, q, q_c):
                return c_node.left
            if o_node.right and addToQueue(o_node.right, c_node.right, q, q_c):
                return c_node.right
        
        return None
