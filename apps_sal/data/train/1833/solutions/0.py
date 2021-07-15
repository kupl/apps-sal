# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # solution with DFS
        def dfs(node, depth):
            if not node:
                return node, depth
            left, l_depth = dfs(node.left, depth + 1)
            right,r_depth = dfs(node.right,depth + 1)
            if l_depth > r_depth:
                return left, l_depth
            if r_depth > l_depth:
                return right,r_depth
            return node,l_depth
        return dfs(root,0)[0]
