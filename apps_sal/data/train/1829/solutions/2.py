class Solution:

    def helper_rec(self, root, tempMax):
        if root is None:
            return
        if root.val >= tempMax:
            self.count += 1
            tempMax = max(root.val, tempMax)
        self.helper_rec(root.left, tempMax)
        self.helper_rec(root.right, tempMax)

    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.count = 0
        self.helper_rec(root, root.val)
        return self.count
