class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def do(node):
            if not node:
                return
            dummy = TreeNode()
            dummy.use = 0
            dummy.covered = dummy.notcovered = 99999

            node.use = 1
            node.covered = 0
            node.notcovered = 0

            do(node.left)
            do(node.right)
            l = node.left
            r = node.right

            ml = min(l.use, l.covered, l.notcovered) if l else 9999
            mr = min(r.use, r.covered, r.notcovered) if r else 9999
            node.use = 1 + (ml if node.left else 0) + (mr if node.right else 0)
            node.covered = min((l.covered if l else 0) + (r.use if r else 9999), (l.use if l else 9999) + (r.covered if r else 0), (l.use if l else 9999) + (r.use if r else 9999))
            node.notcovered = (l.covered if l else 0) + (r.covered if r else 0)

        do(root)
        return 0 if not root else min(root.use, root.covered)
