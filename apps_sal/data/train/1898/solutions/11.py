class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dfs(root: TreeNode, has_parent: bool) -> TreeNode:
            if not root:
                return

            if root.val in to_delete:
                root.left = dfs(root.left, has_parent=False)
                root.right = dfs(root.right, has_parent=False)
                return
            else:
                if not has_parent:
                    result.append(root)
                root.left = dfs(root.left, has_parent=True)
                root.right = dfs(root.right, has_parent=True)
                return root

        result = []
        dfs(root, has_parent=False)
        return result
