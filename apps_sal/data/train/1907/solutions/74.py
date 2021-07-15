# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = TreeNode
    
    def dfs(self, original: TreeNode, cloned: TreeNode, target: TreeNode):
        if original is target:
            self.res = cloned
            return
        print(original.val)
        
        if original.left is None and original.right is None:
            return
        
        if original.left != None:
            print(\"has left\")
            self.dfs(original.left, cloned.left, target)
        if original.right != None:
            print(\"has right\")
            self.dfs(original.right, cloned.right, target)
    
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.dfs(original, cloned, target)
        return self.res
    
