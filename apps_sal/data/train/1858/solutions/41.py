# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root):
        root.val = 0
        self.res = [0]
        
        def dfs(root):
            if root is None:
                return
            if root.left :
                root.left.val = 2*(root.val) + 1
                
                dfs(root.left)
            if root.right :
                root.right.val = 2*(root.val) + 2
                dfs(root.right)
            self.res.append(root.val)
        dfs(root)  
        
    def find(self, target):
        return target in self.res
        
        
        
        
        
        
        
        
        
        
        

