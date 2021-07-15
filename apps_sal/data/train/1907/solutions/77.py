# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if id(original) == id(target):
            return cloned
        
        q = [original]
        p = [cloned]
        idx = 0
        while idx < len(q):
            
            if id(q[idx]) == id(target):
                return p[idx]
            
            if q[idx].left:
                q.append(q[idx].left)
                p.append(p[idx].left)
            if q[idx].right:
                q.append(q[idx].right)
                p.append(p[idx].right)
            
            idx += 1
        
        return None


