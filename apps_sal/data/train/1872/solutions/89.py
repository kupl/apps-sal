import queue


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def dfs(root, height):
            if not root:
                return None
            if len(d) == height:
                d.append(root.val)
            else:
                d[height] += root.val
            dfs(root.left, height + 1)
            dfs(root.right, height + 1)

        d = []
        dfs(root, 0)
        return d.index(max(d)) + 1
