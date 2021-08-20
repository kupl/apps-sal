class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        int_min = -10000000
        ans = self.solve(root, int_min)
        return ans

    def solve(self, root: TreeNode, int_min: int) -> int:
        if root == None:
            return 0
        if root.val < int_min:
            return self.solve(root.left, int_min) + self.solve(root.right, int_min)
        else:
            return self.solve(root.left, root.val) + self.solve(root.right, root.val) + 1
