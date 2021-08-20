class Solution:

    def findDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return 1 + max(self.findDepth(root.left), self.findDepth(root.right))

    def deepestHelper(self, root: TreeNode, c: int, d: int) -> int:
        total = 0
        if root == None:
            return 0
        if c == d:
            return root.val
        return self.deepestHelper(root.left, c + 1, d) + self.deepestHelper(root.right, c + 1, d)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        d = self.findDepth(root)
        return self.deepestHelper(root, 1, d)
