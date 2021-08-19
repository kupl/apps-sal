class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0

        def helper(root, maxm):
            if not root:
                return
            if root.val >= maxm:
                self.cnt += 1
                maxm = root.val
            if root.left:
                helper(root.left, maxm)
            if root.right:
                helper(root.right, maxm)
        maxm = root.val
        helper(root, maxm)
        return self.cnt
