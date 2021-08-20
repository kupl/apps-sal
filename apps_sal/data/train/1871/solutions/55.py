class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.recursiveMax(root, root.val, root.val, 0)

    def recursiveMax(self, root, largest, smallest, max_so_far):
        if root is None:
            return max_so_far
        else:
            diff1 = abs(root.val - largest)
            diff2 = abs(root.val - smallest)
            largest = max(root.val, largest)
            smallest = min(root.val, smallest)
            max_so_far = max(max_so_far, diff1, diff2)
            return max(max_so_far, self.recursiveMax(root.left, largest, smallest, max_so_far), self.recursiveMax(root.right, largest, smallest, max_so_far))
