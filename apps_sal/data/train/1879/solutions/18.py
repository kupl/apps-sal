class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.sum_ = 0
        self.h = self.getHeight(root)

        self.helper(root, 1)
        return self.sum_

    def helper(self, node, height):
        if not node:
            return
        self.helper(node.left, height + 1)
        self.helper(node.right, height + 1)

        if height == self.h:
            self.sum_ += node.val

    def getHeight(self, node):
        if not node:
            return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))
