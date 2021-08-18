class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        self.max_len = 0

        def subTree(root, indir, flip):
            if root is None:
                return 0
            if indir == -1:
                subcount = subTree(root.right, 1, True)
                self.max_len = max(subcount + 1, self.max_len)
            else:
                subcount = subTree(root.left, -1, True)
                self.max_len = max(subcount + 1, self.max_len)

            if flip:
                subTree(root, -indir, False)
            return subcount + 1

        subTree(root, 1, True)
        return self.max_len - 1
