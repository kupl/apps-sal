class Solution:

    def dfs(self, final, root, level):
        if root is None:
            return
        if len(final) < level + 1:
            final.append([])
        final[level].append(root.val)
        self.dfs(final, root.left, level + 1)
        self.dfs(final, root.right, level + 1)

    def maxLevelSum(self, root: TreeNode) -> int:
        final = []
        self.dfs(final, root, 0)
        maxx = max([sum(i) for i in final])
        for i in range(len(final)):
            if sum(final[i]) == maxx:
                return i + 1
        return -1
