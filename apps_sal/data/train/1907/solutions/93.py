# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # 4:41pm
        
#         def sameTree(root1, root2):
#             if not root1 and not root2:
#                 return True
            
#             if root1 and root2:
#                 return root1.val == root2.val and sameTree(root1.left, root2.left) and sameTree(root2.right, root2.right)
        
#         if not original or not cloned:
#             return None
        
#         if original.val == cloned.val == target.val and sameTree(original.left, cloned.left) and sameTree(original.right, cloned.right):
#             return cloned
        
#         return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)

        def dfs(root, target):
            if root and root.val == target:
                return root
            if root:
                return dfs(root.left, target) or dfs(root.right, target)
            
        return dfs(cloned, target.val)
        

