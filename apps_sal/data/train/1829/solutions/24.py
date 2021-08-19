class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        out = [0]

        def _recHelper(curr, maxValue):
            if curr is None:
                return
            if curr.val >= maxValue:
                out[0] += 1
            _recHelper(curr.left, max(curr.val, maxValue))
            _recHelper(curr.right, max(curr.val, maxValue))
        _recHelper(root, -float('inf'))
        return out[0]
