class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)

        def dfs(node, has_parent):
            if not node:
                return False
            if node.val not in to_delete and (not has_parent):
                ans.append(node)
            if dfs(node.left, node.val not in to_delete):
                node.left = None
            if dfs(node.right, node.val not in to_delete):
                node.right = None
            return node.val in to_delete
        dfs(root, False)
        return ans
