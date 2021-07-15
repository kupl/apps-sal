# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def v(node, target_val, acc):
    if node is None:
        return []
    
    if node.val == target_val:
        return acc
    
    return v(node.left, target_val, acc + [-1]) + v(node.right, target_val, acc + [1])
    
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Keep searching the original tree until we find target,
        # keeping track of how we moved to get there
        d = v(original, target.val, [])
        
        node = cloned
        for step in d:
            if step == -1:
                node = node.left
            else:
                node = node.right
        
        return node
