class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        (res, to_delete) = ([], set(to_delete))
        self.dfs(root, res, to_delete, True)
        return res

    def dfs(self, root, res, to_delete, parent_deleted):
        if not root:
            return None
        if parent_deleted and root.val not in to_delete:
            res.append(root)
        root_deleted = True if root.val in to_delete else False
        root.left = self.dfs(root.left, res, to_delete, root_deleted)
        root.right = self.dfs(root.right, res, to_delete, root_deleted)
        return None if root_deleted else root
