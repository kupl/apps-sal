# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, ancestors_values) -> int:
            
            result = [-1]
            this_ancestors_values = [root.val] + ancestors_values
            
            if root.left is not None:
                max_ancestors_diff = max([abs(a - root.left.val) for a in this_ancestors_values])
                left_result = dfs(root.left, this_ancestors_values)
                left_result = max(left_result, max_ancestors_diff)
                result.append(left_result)
            if root.right is not None:
                max_ancestors_diff = max([abs(a - root.right.val) for a in this_ancestors_values])
                right_result = dfs(root.right, this_ancestors_values)
                right_result = max(right_result, max_ancestors_diff)
                result.append(right_result)
            
            return max(result)
            
        result = dfs(root, [])
        return result

