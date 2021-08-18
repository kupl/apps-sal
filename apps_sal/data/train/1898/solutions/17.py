class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        res = set([root])

        deleteSet = set(to_delete)

        def dfs(root):

            if not root:
                return

            if root.val in deleteSet:
                if root in res:
                    res.remove(root)
                if root.left:
                    res.add(root.left)
                if root.right:
                    res.add(root.right)

            dfs(root.left)
            dfs(root.right)

            if root.left and root.left.val in deleteSet:
                root.left = None
            if root.right and root.right.val in deleteSet:
                root.right = None

        dfs(root)

        return list(res)
