class Solution:

    def longestZigZag(self, root: TreeNode) -> int:

        def Search(root, left, height):
            if root is None:
                return height
            if left:
                return max(Search(root.left, 1, 0), Search(root.right, 0, height + 1))
            else:
                return max(Search(root.right, 0, 0), Search(root.left, 1, height + 1))
        return max(Search(root.left, 1, 0), Search(root.right, 0, 0))
