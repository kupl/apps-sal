# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        sums = collections.defaultdict(int)
        visited = []
        
        def dfs(root, level):
            if root:
                sums[level] += root.val
                visited.append(root)

                dfs(root.right, level + 1)
                dfs(root.left, level + 1)
        
        dfs(root, 1)
        return max(sums, key=sums.get)
