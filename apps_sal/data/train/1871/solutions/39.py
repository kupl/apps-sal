# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.v_max = 0
        
        def find(node, path):
            if not node:                
                return 
 
            tmp = max(abs(max(path) - node.val), abs(min(path) - node.val))
            self.v_max = max(self.v_max, tmp)
            
            path.append(node.val)
            
            find(node.left, path)
            find(node.right, path)
            
            path.pop()
            
        find(root, [root.val])
        return self.v_max
