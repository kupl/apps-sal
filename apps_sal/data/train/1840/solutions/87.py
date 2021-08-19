class Solution:

    def longestZigZag(self, root: TreeNode) -> int:

        def dfs(root):
            if root is None:
                return (0, [0, 0])
            (left_zigzag, [_, right]) = dfs(root.left)
            (right_zigzag, [left, _]) = dfs(root.right)
            zigzag = max(left_zigzag, right_zigzag)
            if root.right:
                right_zigzag = 1 + left
                zigzag = max(zigzag, right_zigzag)
            else:
                right_zigzag = 0
            if root.left:
                left_zigzag = 1 + right
                zigzag = max(zigzag, left_zigzag)
            else:
                left_zigzag = 0
            return (zigzag, [left_zigzag, right_zigzag])
        return dfs(root)[0]
