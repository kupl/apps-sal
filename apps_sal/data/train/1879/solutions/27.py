class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.sum = 0
        self.deepest_lvl = 0

        def bfs(root: TreeNode, lvl=0):
            if root is None:
                return
            if root.left is None and root.right is None:
                print(root.val, lvl)
                if lvl > self.deepest_lvl:
                    self.sum = root.val
                    self.deepest_lvl = lvl
                elif lvl == self.deepest_lvl:
                    self.sum += root.val
                return
            bfs(root.left, lvl + 1)
            bfs(root.right, lvl + 1)
        bfs(root)
        return self.sum
