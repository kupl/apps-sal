class Solution:
    counter = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0
        self._goodNodes(root, root.val)
        return self.counter

    def _goodNodes(self, root: TreeNode, current_max: int):
        if not root:
            return
        if root.val >= current_max:
            self.counter += 1
        self._goodNodes(root.left, max(current_max, root.val))
        self._goodNodes(root.right, max(current_max, root.val))
