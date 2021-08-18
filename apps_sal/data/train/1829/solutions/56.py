class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, path):

            if root:
                indx = bisect.bisect(path, root.val)
                if indx == len(path):
                    self.count += 1
                dfs(root.left, path[:indx] + [root.val] + path[indx:])
                dfs(root.right, path[:indx] + [root.val] + path[indx:])
        self.count = 0
        dfs(root, [])
        return self.count
