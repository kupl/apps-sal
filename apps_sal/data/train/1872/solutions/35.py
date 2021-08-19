class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        res = []
        level = 0

        def dfs(root, res, level):
            if root == None:
                return
            if level >= len(res):
                res.append(0)
            res[level] += root.val
            level += 1
            dfs(root.left, res, level)
            dfs(root.right, res, level)
        dfs(root, res, level)
        return res.index(max(res)) + 1
