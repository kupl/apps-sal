class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.count = 0
        self._goodNodes(root, root.val)
        return self.count

    def _goodNodes(self, curNode, curGreatest):
        if curNode == None:
            return
        if curNode.val >= curGreatest:
            self.count += 1

        self._goodNodes(curNode.left, max(curNode.val, curGreatest))
        self._goodNodes(curNode.right, max(curNode.val, curGreatest))
