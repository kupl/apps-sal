class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGoodNodes(root, -999999)

    def countGoodNodes(self, node, maxSoFar):
        if node is None:
            return 0

        newMax = max(maxSoFar, node.val)
        return int(node.val >= maxSoFar) + self.countGoodNodes(node.left, newMax) + self.countGoodNodes(node.right, newMax)
