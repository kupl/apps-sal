class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return(self.helper(root))

    def helper(self, root, maxVal=-9999):
        total = 0
        if root.val >= maxVal:
            total += 1
            maxVal = root.val
        if root.left:
            total += self.helper(root.left, maxVal)
        if root.right:
            total += self.helper(root.right, maxVal)

        return total
