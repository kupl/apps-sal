class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(self.length(root.left, 'l', 1), self.length(root.right, 'r', 1))

    def length(self, node, d, depth):
        if not node:
            return depth - 1
        print((d, depth, node.val))

        if d == 'l':
            return max(self.length(node.right, 'r', depth + 1), self.length(node.left, 'l', 1))
        else:
            return max(self.length(node.left, 'l', depth + 1), self.length(node.right, 'r', 1))
