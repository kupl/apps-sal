class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        sumNode = []
        self.goodNode(root, -234627, sumNode)
        return len(sumNode)

    def goodNode(self, root, maxSoFar, sumNode):
        if root is None:
            return
        print(root.val)
        if root.val >= maxSoFar:
            sumNode.append(root.val)
        maxSoFarNow = max(maxSoFar, root.val)
        self.goodNode(root.left, maxSoFarNow, sumNode)
        self.goodNode(root.right, maxSoFarNow, sumNode)
