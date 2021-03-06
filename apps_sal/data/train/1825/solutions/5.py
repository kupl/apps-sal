class Solution:

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        def get_depth(root):
            if not root:
                return 0
            else:
                return max(get_depth(root.left), get_depth(root.right)) + 1
        max_depth = get_depth(root)

        def dfs(root, depth):
            if not root:
                return root
            if get_depth(root.left) == get_depth(root.right) == depth - 1:
                return root
            return dfs(root.left, depth - 1) or dfs(root.right, depth - 1)
        return dfs(root, max_depth)
