# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def parsePath(self, s):
        depth = 0
        path = [0]
        for x in s:
            if x != \"-\" and depth > 0:
                path.append(depth)
                depth = 0
            elif x == \"-\":
                depth += 1
        return path
    
    def recoverFromPreorder(self, S: str) -> TreeNode:
        vals = [int(n) for n in filter(lambda x: x != \"\", S.split(\"-\"))]
        if len(vals) == 1:
            return TreeNode(vals[0])
        path = self.parsePath(S)
        stack = deque()
        
        print(path, vals)
        
        depth = i = 0
        root = node = None
        while i < len(path):
            if not root:
                root = TreeNode(vals[i])
                node = root
                i += 1
            
            if depth < path[i]:
                stack.append(node)
                if not node.left:
                    node.left = TreeNode(vals[i])
                    node = node.left
                else:
                    node.right = TreeNode(vals[i])
                    node = node.right
                depth += 1
                i += 1
            else:
                node = stack.pop()
                depth -= 1
            
        return root
        
