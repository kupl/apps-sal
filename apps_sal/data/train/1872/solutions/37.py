class Solution:

    def ht(self, root):
        if root == None:
            return 0
        return 1 + max(self.ht(root.left), self.ht(root.right))

    def Sum(self, root, SA, level):
        if root != None:
            print(level)
            SA[level] += root.val
            if root.left != None:
                self.Sum(root.left, SA, level + 1)
            if root.right != None:
                self.Sum(root.right, SA, level + 1)

    def maxLevelSum(self, root: TreeNode) -> int:
        SA = [0] * self.ht(root)
        self.Sum(root, SA, 0)
        return SA.index(max(SA)) + 1
