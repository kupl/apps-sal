class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.recursiveMax(root, root.val, root.val)

    def recursiveMax(self, root, largest, smallest):
        if root is None:
            return 0
        else:
            diff1 = abs(root.val - largest)
            diff2 = abs(root.val - smallest)
            largest = max(root.val, largest)
            smallest = min(root.val, smallest)
            return max(diff1, diff2, self.recursiveMax(root.left, largest, smallest), self.recursiveMax(root.right, largest, smallest))
