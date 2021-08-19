
# 1372. Longest ZigZag Path in a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                # [left, right, res]
                return [-1, -1, -1]
            left, right = dfs(root.left), dfs(root.right)
            # [left.right + 1, right.left + 1, max(left.right + 1, right.left + 1, left.res, right.res)]
            return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]

        return dfs(root)[-1]

# Explanation
# Recursive return [left, right, result], where:
# left is the maximum length in direction of root.left
# right is the maximum length in direction of root.right
# result is the maximum length in the whole sub tree.


# Complexity
# Time O(N)
# Space O(height)
