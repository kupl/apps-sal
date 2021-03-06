class Solution:

    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0
        seen = set()
        self.ans = 0

        def inorder(root, parent=None):
            if root:
                inorder(root.left, root)
                inorder(root.right, root)
                for i in [parent, root, root.left, root.right]:
                    if i and i in seen:
                        break
                else:
                    self.ans += 1
                    seen.update(set([parent, root, root.left, root.right]))
        inorder(root)
        return self.ans
