# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if not original:
            return None
        
        stack = []
        
        def dfs( curr ):                                                
            
            if curr == target:
                return True
            
            if curr.left:
                stack.append(\"L\")
                if dfs(curr.left):
                    return True
                stack.pop()
                
            if curr.right:
                stack.append(\"R\")
                if dfs(curr.right):
                    return True
                stack.pop()      
                
            return False
        
        dfs(original)
        for d in stack:            
            if d == \"L\":
                cloned = cloned.left
            else:
                cloned = cloned.right
                            
                
        return cloned
            
            
            
