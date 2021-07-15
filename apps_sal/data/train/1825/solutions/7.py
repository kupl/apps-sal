# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def traverse(root, level):
            if root:
                if not root.left and not root.right:
                    return level, root
                else:
                    left_level, left_lca = traverse(root.left, level + 1)
                    right_level, right_lca = traverse(root.right, level + 1)
                    if left_level == right_level:
                        return left_level, root
                    elif left_level > right_level:
                        return left_level, left_lca
                    else:
                        return right_level, right_lca
            return float('-inf'), None

        deepest_level, lca = traverse(root, 0)
        return lca
