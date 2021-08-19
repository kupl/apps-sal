class Solution:

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        elif val > root.val:
            n = TreeNode(val)
            n.left = root
            return n
        else:
            n = root
            p = None
            while n is not None and val < n.val:
                (n, p) = (n.right, n)
            m = TreeNode(val)
            p.right = m
            m.left = n
            return root
