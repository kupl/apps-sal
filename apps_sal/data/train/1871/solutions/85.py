class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_val = 0

        def traversal(root, parent):

            if not root:
                return
            for i in parent:

                if self.max_val < abs(i - root.val):
                    self.max_val = abs(i - root.val)
            if root.left:
                traversal(root.left, parent + [root.val])
            if root.right:
                traversal(root.right, parent + [root.val])
            return
        traversal(root, [])
        return self.max_val
