class Solution:

    def sufficientSubset(self, root, limit):

        def dfs(root, cur):
            if root is None:
                return None
            s = root.val + cur
            if root.left is None and root.right is None:
                if s < limit:
                    return None
                else:
                    return root
            l = dfs(root.left, s)
            r = dfs(root.right, s)
            if l is None and r is None:
                return None
            (root.left, root.right) = (l, r)
            return root
        return dfs(root, 0)
